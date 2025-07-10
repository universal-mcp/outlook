import asyncio
import json
import os
from typing import Any, Dict, List, Optional
from openai import AzureOpenAI
from dotenv import load_dotenv
from universal_mcp_outlook.app import OutlookApp
from universal_mcp.integrations import AgentRIntegration
from universal_mcp.tools import ToolManager

from langgraph.graph import StateGraph, END, START
from typing_extensions import TypedDict
import uuid
import pytest

load_dotenv()

langsmith_api_key = os.getenv("LANGCHAIN_API_KEY")
if langsmith_api_key:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "app-agent-automation")
    print("🔍 LangSmith tracing enabled")
else:
    print("⚠️  LangSmith tracing disabled - set LANGCHAIN_API_KEY to enable")


class AgentState(TypedDict):
    """State representation for the agent during debugging.

    Tracks the conversation messages, user prompt, current step in the workflow,
    results from tool executions, and completion status.
    """
    messages: List[Dict]
    user_prompt: str
    current_step: int
    tool_results: List[Dict[str, Any]]
    is_complete: bool


class AppAgent:
    """Self-contained Outlook agent with LLM tool calling and LangGraph workflow"""
    
    def __init__(self):
        """Initialize agent with all necessary components from environment variables"""
        
        # Setup AgentR integration 
        agentr_api_key = os.getenv("AGENTR_API_KEY")
        if not agentr_api_key:
            raise ValueError("AGENTR_API_KEY environment variable is required")
        
        self.integration = AgentRIntegration(name="outlook", api_key=agentr_api_key, base_url="https://api.agentr.dev")
        self.app = OutlookApp(integration=self.integration)
        
        # Setup Azure OpenAI client
        azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        if not azure_api_key or not azure_endpoint:
            raise ValueError("Azure OpenAI credentials required: AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT")
        
        self.model = os.getenv("OPEN_AI_MODEL", "o4-mini")
        self.client = AzureOpenAI(
            api_key=azure_api_key,
            azure_endpoint=azure_endpoint,
            api_version="2025-03-01-preview"
        )
        
        # Setup tool manager and workflow
        self.tool_manager = ToolManager()
        self._setup_tools()
        # Don't initialize workflow here - it will be built per request
        
        print(f"🎭 App Agent initialized successfully")
        print(f"🔗 AgentR Base URL: https://api.agentr.dev")
        
    def _setup_tools(self):
        """Setup tools in tool manager using SDK"""
        # Define selected tools directly 
        selected_tools = ["user_list_message", "user_send_mail", "user_get_message", "user_delete_message", "users_message_reply"]  # Modify this array to add/remove tools
        
        # Add only the selected tools directly
        for tool_name in selected_tools:
            if hasattr(self.app, tool_name):
                tool_func = getattr(self.app, tool_name)
                self.tool_manager.add_tool(tool_func)
    
    def _get_tool_descriptions(self) -> str:
        """Get formatted tool descriptions for LLM using SDK"""
        tools_info = []
        all_tools = self.tool_manager.get_tools_by_app()
        
        for tool in all_tools:
            params = []
            if tool.parameters:
                if isinstance(tool.parameters, dict):
                    for param_name, param_info in tool.parameters.items():
                        if isinstance(param_info, dict):
                            param_type = param_info.get('type', 'str')
                        else:
                            param_type = str(param_info)
                        params.append(f"{param_name}: {param_type}")
                elif isinstance(tool.parameters, list) and tool.parameters:
                    for param in tool.parameters:  # type: ignore
                        if isinstance(param, dict):
                            param_name = param.get('name', 'unknown')
                            param_type = param.get('type', 'str')
                            params.append(f"{param_name}: {param_type}")
                        else:
                            params.append(str(param))
            
            tool_info = f"""
Tool: {tool.name}
Description: {tool.description or 'No description available'}
Arguments: {tool.args_description or 'No arguments description'}
Returns: {tool.returns_description or 'No returns description'}
Parameters: {', '.join(params) if params else 'No parameters'}
Full Parameters Schema: {tool.parameters}
"""
            tools_info.append(tool_info)
        
        return '\n'.join(tools_info)
    

    
    async def _planner_node(self, state: AgentState, prompt_index: int) -> AgentState:
        """Plan what tool to use with context from previous tool executions"""
        user_prompt = state["user_prompt"]
        tools_desc = self._get_tool_descriptions()
        
        # Build context from previous tool results
        context_from_previous_tools = ""
        if state["tool_results"]:
            context_from_previous_tools = "\n\nPrevious tool executions in this session:\n"
            for i, tool_result in enumerate(state["tool_results"]):
                if tool_result["status"] == "success":
                    context_from_previous_tools += f"- Step {i+1}: Used {tool_result['tool']} with args {tool_result['arguments']} → Result: {tool_result['result']}\n"
                else:
                    context_from_previous_tools += f"- Step {i+1}: Failed to use {tool_result['tool']} → Error: {tool_result.get('error', 'Unknown error')}\n"
        
        system_prompt = f"""You are an app assistant. Based on the user's request, you need to:
1. Choose the appropriate tool from the available tools
2. Provide the correct arguments for that tool

Available tools:
{tools_desc}

{context_from_previous_tools}

IMPORTANT: You must respond in this EXACT format:
TOOL: tool_name
ARGUMENTS: {{"param1": "value1", "param2": "value2"}}

RULES:
- Keep arguments minimal and only include what's necessary for the user's request so required parameters only unless a user specifies the other parameters
- You can reference results from previous tool executions if relevant to the current request
- Each request should be handled independently unless there's a clear relationship to previous results

User request: {user_prompt}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        
        llm_response = response.choices[0].message.content
        
        new_state = state.copy()
        new_state["messages"].append({
            "role": "assistant", 
            "content": llm_response,
            "prompt": user_prompt,
            "prompt_index": prompt_index
        })
        
        return new_state
    
    async def _executor_node(self, state: AgentState, prompt_index: int) -> AgentState:
        """Execute the planned tool with context tracking"""
        # Find the latest message for this prompt
        relevant_messages = [msg for msg in state["messages"] if msg.get("prompt_index") == prompt_index]
        if not relevant_messages:
            new_state = state.copy()
            new_state["tool_results"].append({
                "error": "No LLM response found for execution",
                "status": "error",
                "prompt_index": prompt_index
            })
            return new_state
            
        llm_response = relevant_messages[-1]["content"]
        user_prompt = relevant_messages[-1]["prompt"]
        
        tool_name, arguments = self._parse_llm_response(llm_response)
        
        if tool_name and arguments is not None:
            try:
                result = await self.tool_manager.call_tool(
                    name=tool_name,
                    arguments=arguments
                )
                
                new_state = state.copy()
                new_state["tool_results"].append({
                    "tool": tool_name,
                    "arguments": arguments,
                    "result": result,
                    "status": "success",
                    "prompt": user_prompt,
                    "prompt_index": prompt_index
                })
                
                return new_state
                
            except Exception as e:
                new_state = state.copy()
                new_state["tool_results"].append({
                    "tool": tool_name,
                    "arguments": arguments,
                    "error": str(e),
                    "status": "error",
                    "prompt": user_prompt,
                    "prompt_index": prompt_index
                })
                
                return new_state
        else:
            new_state = state.copy()
            new_state["tool_results"].append({
                "error": "Failed to parse LLM response",
                "llm_response": llm_response,
                "status": "error",
                "prompt": user_prompt,
                "prompt_index": prompt_index
            })
            
            return new_state
    
    def _parse_llm_response(self, response: str) -> tuple[Optional[str], Optional[Dict]]:
        """Parse LLM response to extract tool name and arguments"""
        try:
            lines = response.strip().split('\n')
            tool_name = None
            arguments = None
            
            for line in lines:
                line = line.strip()
                if line.startswith('TOOL:'):
                    tool_name = line.replace('TOOL:', '').strip()
                elif line.startswith('ARGUMENTS:'):
                    args_str = line.replace('ARGUMENTS:', '').strip()
                    arguments = json.loads(args_str)
            
            return tool_name, arguments
            
        except Exception as e:
            print(f"Error parsing LLM response: {e}")
            return None, None
    
    async def process_request(self, user_prompt: str) -> Dict[str, Any]:
        """Process single user request through the LangGraph workflow"""
        # Use the multiple request workflow with a single prompt
        return await self.process_multiple_requests([user_prompt])

    async def process_multiple_requests(self, prompts: List[str]) -> Dict[str, Any]:
        """Process multiple user requests in a single trace"""
        # Generate a single trace ID for all requests
        trace_id = str(uuid.uuid4())
        
        print(f"🔍 Single trace ID for all prompts: {trace_id}")
        
        all_results = []
        
        # Create a single workflow that processes all prompts
        combined_workflow = self._build_workflow(prompts)
        
        initial_state = AgentState(
            messages=[],
            user_prompt="",  # Will be set per prompt
            current_step=0,
            tool_results=[],
            is_complete=False
        )
        
        try:
            # Execute all prompts in a single workflow trace
            final_state = await combined_workflow.ainvoke(initial_state)
            
            return {
                "success": True,
                "prompts": prompts,
                "tool_results": final_state["tool_results"],
                "llm_messages": final_state["messages"],
                "trace_id": trace_id
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "prompts": prompts,
                "trace_id": trace_id
            }
    
    def _build_workflow(self, prompts: List[str]):
        """Build workflow that processes single or multiple prompts sequentially in one trace with tool chaining"""
        workflow = StateGraph(AgentState)
        
        # Add nodes for each prompt - reuse existing planner/executor logic
        for i, prompt in enumerate(prompts):
            planner_node_name = f"planner_{i}"
            executor_node_name = f"executor_{i}"
            
            # Create closures to capture the prompt and enable tool chaining
            def make_planner_node(prompt_text, prompt_index):
                async def planner_node(state: AgentState) -> AgentState:
                    print(f"\n🔄 Processing prompt {prompt_index + 1}/{len(prompts)}: {prompt_text}")
                    # Update state with current prompt and use existing planner logic with tool chaining
                    new_state = state.copy()
                    new_state["user_prompt"] = prompt_text
                    return await self._planner_node(new_state, prompt_index)
                return planner_node
            
            def make_executor_node(prompt_index):
                async def executor_node(state: AgentState) -> AgentState:
                    return await self._executor_node(state, prompt_index)
                return executor_node
            
            workflow.add_node(planner_node_name, make_planner_node(prompt, i))
            workflow.add_node(executor_node_name, make_executor_node(i))
        
        # Connect the nodes sequentially
        workflow.add_edge(START, "planner_0")
        
        for i in range(len(prompts)):
            planner_node_name = f"planner_{i}"
            executor_node_name = f"executor_{i}"
            
            workflow.add_edge(planner_node_name, executor_node_name)
            
            if i < len(prompts) - 1:
                next_planner = f"planner_{i + 1}"
                workflow.add_edge(executor_node_name, next_planner)
            else:
                workflow.add_edge(executor_node_name, END)
        
        return workflow.compile()
    



# Simple test function
@pytest.mark.asyncio
async def test_app_agent():
    """Test the app agent with full automation workflow"""
    
    print("🚀 Testing App Agent - Tool Descriptions")
    print("=" * 50)
    
    test_passed = False
    
    try:
        # Initialize agent (all setup handled internally)
        agent = AppAgent()
        
        # Print tool descriptions to verify they're working correctly
        print("📋 Tool Descriptions:")
        print("=" * 50)
        tool_descriptions = agent._get_tool_descriptions()
        print(tool_descriptions)
        print("=" * 50)
        
        # Array of prompts to execute sequentially
        test_prompts = [
            "list my 3 emails, and check if i have received any emails from rshvraj36@gmail.com, For user_id parameter, always use rishabh@agentr.dev unless specified otherwise",
            "Send a reply to that message with message hey how are you"
        ]
        
        print(f"📝 Executing {len(test_prompts)} prompts sequentially in a single trace:")
        print("-" * 50)
        
        # Process all prompts in a single trace
        result = await agent.process_multiple_requests(test_prompts)
        
        if result["success"]:
            print("✅ All prompts processed successfully!")
            
            if os.getenv("LANGCHAIN_API_KEY"):
                print(f"🔍 Single Trace ID: {result.get('trace_id', 'N/A')}")
              
            
            # Display results for each prompt
            if result["tool_results"]:
                print("\n📋 TOOL EXECUTION RESULTS:")
                print("=" * 50)
                
                for tool_result in result["tool_results"]:
                    prompt_num = tool_result.get("prompt_index", 0) + 1
                    prompt_text = tool_result.get("prompt", "Unknown prompt")
                    
                    print(f"\n🔄 Prompt {prompt_num}: {prompt_text}")
                    print("-" * 30)
                    
                    if tool_result["status"] == "success":
                        print(f"✅ Tool: {tool_result['tool']}")
                        print(f"📝 Arguments: {tool_result['arguments']}")
                        print(f"📊 Result: {tool_result['result']}")
                    else:
                        print(f"❌ Tool Error: {tool_result.get('error', 'Unknown error')}")
            
            # Summary
            successful_tools = sum(1 for result in result["tool_results"] if result["status"] == "success")
            failed_tools = len(result["tool_results"]) - successful_tools
            
            print(f"\n📊 EXECUTION SUMMARY:")
            print("=" * 50)
            print(f"✅ Successful tool calls: {successful_tools}/{len(result['tool_results'])}")
            print(f"❌ Failed tool calls: {failed_tools}/{len(result['tool_results'])}")
            
            if failed_tools > 0:
                print(f"\n❌ TEST FAILED: {failed_tools} out of {len(result['tool_results'])} tool calls failed")
                print("📋 Failed tool details:")
                for i, tool_result in enumerate(result["tool_results"]):
                    if tool_result["status"] == "error":
                        prompt_num = tool_result.get("prompt_index", 0) + 1
                        print(f"  - Prompt {prompt_num}: {tool_result.get('error', 'Unknown error')}")
                
                raise AssertionError(f"Tool execution failed: {failed_tools}/{len(result['tool_results'])} tool calls failed")
            
            test_passed = True
            print(f"\n✅ All {successful_tools} tool calls completed successfully!")
            
        else:
            print(f"❌ Workflow failed: {result['error']}")
            if os.getenv("LANGCHAIN_API_KEY"):
                print(f"🔍 Trace ID: {result.get('trace_id', 'N/A')}")
            
            raise AssertionError(f"Workflow execution failed: {result['error']}")
    
    except Exception as e:
        print(f"❌ Test failed: {e}")
        raise  
    
    if not test_passed:
        raise AssertionError("Test did not complete successfully")
    
    print("🎉 Sequential prompt execution in single trace completed successfully!")
    return True


async def main():
    """Main function"""
    try:
        await test_app_agent()
        print("✅ All tests passed!")
        exit(0)  # Success exit code
    except Exception as e:
        print(f"❌ Tests failed: {e}")
        exit(1)  # Failure exit code


if __name__ == "__main__":
    asyncio.run(main())