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
        agentr_base_url = os.getenv("AGENTR_BASE_URL")
        app_name = os.getenv("APP_NAME", "outlook")  # Default to outlook, can be overridden
        if not agentr_api_key:
            raise ValueError("AGENTR_API_KEY environment variable is required")
        
        integration_kwargs = {"name": app_name, "api_key": agentr_api_key}
        if agentr_base_url:
            integration_kwargs["base_url"] = agentr_base_url
        
        self.integration = AgentRIntegration(**integration_kwargs)
        self.app = OutlookApp(integration=self.integration)  # This can be changed for different apps
        
        # Setup Azure OpenAI client
        azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        azure_deployment = os.getenv("OPEN_AI_MODEL", "o4-mini")
        api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2025-03-01-preview")
        
        if not azure_api_key or not azure_endpoint:
            raise ValueError("Azure OpenAI credentials required: AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT")
        
        self.model = azure_deployment
        self.client = AzureOpenAI(
            api_key=azure_api_key,
            azure_endpoint=azure_endpoint,
            api_version=api_version
        )
        
        # Setup tool manager and workflow
        self.tool_manager = ToolManager()
        self._setup_tools()
        self.workflow = self._build_workflow()
        
        print(f"🎭 App Agent initialized successfully")
        if agentr_base_url:
            print(f"🔗 AgentR Base URL: {agentr_base_url}")
        
    def _setup_tools(self):
        """Setup tools in tool manager using SDK"""
        available_tools = self.app.list_tools()
        for tool_func in available_tools:
            self.tool_manager.add_tool(tool_func)
    
    def _get_tool_descriptions(self) -> str:
        """Get formatted tool descriptions for LLM using SDK"""
        tools_info = []
        all_tools = self.tool_manager.get_tools_by_app()
        
        for tool in all_tools:
            # Format parameters for display
            params = []
            if tool.parameters:
                # Handle both dict and list formats for parameters
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
    
    def _build_workflow(self):
        """Build simplified workflow"""
        workflow = StateGraph(AgentState)
        
        workflow.add_node("planner", self._planner_node)
        workflow.add_node("executor", self._executor_node)
        
        workflow.add_edge(START, "planner")
        workflow.add_edge("planner", "executor")
        workflow.add_edge("executor", END)
        
        return workflow.compile()
    
    async def _planner_node(self, state: AgentState) -> AgentState:
        """Plan what tool to use and with what arguments"""
        user_prompt = state["user_prompt"]
        tools_desc = self._get_tool_descriptions()
        
        system_prompt = f"""You are an app assistant. Based on the user's request, you need to:
1. Choose the appropriate tool from the available tools
2. Provide the correct arguments for that tool

Available tools:
{tools_desc}

IMPORTANT: You must respond in this EXACT format:
TOOL: tool_name
ARGUMENTS: {{"param1": "value1", "param2": "value2"}}

RULES:
- Keep arguments minimal and only include what's necessary for the user's request so required parameters only unless a user specifies the other parameters

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
        new_state["messages"].append({"role": "assistant", "content": llm_response})
        
        return new_state
    
    async def _executor_node(self, state: AgentState) -> AgentState:
        """Execute the planned tool"""
        llm_response = state["messages"][-1]["content"]
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
                    "status": "success"
                })
                new_state["is_complete"] = True
                
                return new_state
                
            except Exception as e:
                new_state = state.copy()
                new_state["tool_results"].append({
                    "tool": tool_name,
                    "arguments": arguments,
                    "error": str(e),
                    "status": "error"
                })
                new_state["is_complete"] = True
                
                return new_state
        else:
            new_state = state.copy()
            new_state["tool_results"].append({
                "error": "Failed to parse LLM response",
                "llm_response": llm_response,
                "status": "error"
            })
            new_state["is_complete"] = True
            
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
        """Process user request through the LangGraph workflow"""
        # Generate a unique trace ID for this request
        trace_id = str(uuid.uuid4())
        
        initial_state = AgentState(
            messages=[],
            user_prompt=user_prompt,
            current_step=0,
            tool_results=[],
            is_complete=False
        )
        
        try:
            # Add metadata for LangSmith tracing
            final_state = await self.workflow.ainvoke(initial_state)
            
            return {
                "success": True,
                "user_prompt": user_prompt,
                "tool_results": final_state["tool_results"],
                "llm_messages": final_state["messages"],
                "trace_id": trace_id
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "user_prompt": user_prompt,
                "trace_id": trace_id
            }


# Simple test function
async def test_app_agent():
    """Test the app agent with full automation workflow"""
    
    print("🚀 Testing App Agent - Tool Descriptions")
    print("=" * 50)
    
    try:
        # Initialize agent (all setup handled internally)
        agent = AppAgent()
        
        # Print tool descriptions to verify they're working correctly
        print("📋 Tool Descriptions:")
        print("=" * 50)
        tool_descriptions = agent._get_tool_descriptions()
        print(tool_descriptions)
        print("=" * 50)
        
        test_prompt = "list my 3 emails, For user_id parameter, always use rishabh@agentr.dev unless specified otherwise"
        print(f"Testing: {test_prompt}")
        print("-" * 50)
        
        result = await agent.process_request(test_prompt)
        
        if result["success"]:
            print("✅ Success!")
            
            if os.getenv("LANGCHAIN_API_KEY"):
                print(f"🔍 Trace ID: {result.get('trace_id', 'N/A')}")
                project_name = os.getenv("LANGCHAIN_PROJECT", "app-agent-automation")
                print(f"📊 View trace at: https://smith.langchain.com/traces/{result.get('trace_id', 'N/A')}")
                print(f"🌐 Project: https://smith.langchain.com/o/default/p/{project_name}")
            
            if result["llm_messages"]:
                llm_response = result["llm_messages"][-1]["content"]
                print(f"LLM Response:\n{llm_response}")
            
            if result["tool_results"]:
                tool_result = result["tool_results"][0]
                if tool_result["status"] == "success":
                    print(f"Tool: {tool_result['tool']}")
                    print(f"Arguments: {tool_result['arguments']}")
                    print(f"Result: {tool_result['result']}")
                else:
                    print(f"Tool Error: {tool_result.get('error', 'Unknown error')}")
        else:
            print(f"❌ Failed: {result['error']}")
            if os.getenv("LANGCHAIN_API_KEY"):
                print(f"🔍 Trace ID: {result.get('trace_id', 'N/A')}")
            
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        print("\nMake sure you have these environment variables set:")
        print("  - AZURE_OPENAI_API_KEY")
        print("  - AZURE_OPENAI_ENDPOINT") 
        print("  - OPEN_AI_MODEL (optional, defaults to 'o4-mini')")
        print("  - AGENTR_API_KEY")
        print("  - AGENTR_BASE_URL (optional)")
        print("  - APP_NAME (optional, defaults to 'outlook')")
        print("  - LANGCHAIN_API_KEY (optional, for LangSmith visualization)")


async def main():
    """Main function"""
    await test_app_agent()


if __name__ == "__main__":
    asyncio.run(main())