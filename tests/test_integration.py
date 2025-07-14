import os
import pytest
import asyncio
from dataclasses import dataclass
from typing import List, Optional
from pydantic import SecretStr

from langchain_core.messages import HumanMessage, AIMessage
from langgraph.prebuilt import create_react_agent

from universal_mcp.tools import ToolManager
from universal_mcp.tools.adapters import ToolFormat
from universal_mcp_outlook.app import OutlookApp
from universal_mcp.integrations import AgentRIntegration


@dataclass
class TestCase:
    app: str
    tools: Optional[List[str]] = None
    tasks: Optional[List[str]] = None
    validate_query: Optional[str] = None


def load_app(app_name: str):
    """Load application instance with real integration."""
    if app_name == "outlook":
        integration = AgentRIntegration(
            name="outlook", 
            api_key=os.environ.get("AGENTR_API_KEY"),
            base_url=os.environ.get("AGENTR_BASE_URL", "https://api.agentr.dev")
        )
        
        app_instance = OutlookApp(integration=integration)
        return app_instance
    else:
        raise ValueError(f"Unsupported app: {app_name}")


async def execute_case(test_case: TestCase):
    """Execute a test case using LangGraph ReAct agent."""
    tool_manager = ToolManager()
    
    app_instance = load_app(test_case.app)
    
    all_tools = app_instance.list_tools()
    print(f"Available tools from app: {[getattr(t, '__name__', str(t)) for t in all_tools]}")
    
    tool_manager.register_tools_from_app(app_instance)
    
    all_registered = tool_manager.get_tools_by_app(app_name=app_instance.name)
    print(f"All registered tools: {[t.name for t in all_registered]}")
    
    if test_case.tools:
        tools = tool_manager.list_tools(
            format=ToolFormat.LANGCHAIN,
            app_name=app_instance.name,
            tool_names=test_case.tools
        )
    else:
        tools = tool_manager.list_tools(
            format=ToolFormat.LANGCHAIN,
            app_name=app_instance.name
        )
    
    print(f"Tools for test: {[tool.name for tool in tools]}")
    
    azure_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    azure_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    azure_deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "o4-mini")
    api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2025-03-01-preview")
    
    if not azure_endpoint or not azure_api_key:
        raise ValueError(
            "Azure OpenAI credentials not found. Please set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_API_KEY environment variables."
        )
    
    try:
        from langchain_openai import AzureChatOpenAI
        llm = AzureChatOpenAI(
            azure_endpoint=azure_endpoint,
            azure_deployment=azure_deployment,
            api_key=SecretStr(azure_api_key) if azure_api_key else None,
            api_version=api_version,
        )
        print(f"Using Azure OpenAI with deployment: {azure_deployment}")
    except ImportError:
        print("langchain_openai not found, falling back to default model")
        llm = "gpt-4o-mini"
    
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt="You are a helpful assistant that can use the following tools: {tools}. Always respond in natural language after using tools. Summarize what you did and what you found."
    )
    
    messages = []
    for task in test_case.tasks or []:
        try:
            messages.append(HumanMessage(content=task))
            response = await agent.ainvoke({"messages": messages})
            messages.append(AIMessage(content=response["messages"][-1].content))
            print(f"Task: {task}")
            print(f"Response: {response['messages'][-1].content}")
            print("---")
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
            assert False

    if test_case.validate_query:
        messages.append(HumanMessage(content=test_case.validate_query + " Answer with yes or no and explain why."))
        response = await agent.ainvoke({"messages": messages})
        response_text = response["messages"][-1].content.lower()
        print(f"Validation query: {test_case.validate_query}")
        print(f"Response: {response_text}")
        assert any(word in response_text for word in ["yes", "true", "correct", "successfully"]), f"Validation failed: {response_text}"


outlook_test_case = TestCase(
    app="outlook",
    tools=["user_send_mail", "user_list_message"],
    tasks=[
        "Send an email to rshvraj36@gmail.com saying subject: hello and message: hey what are you upto. use user_id: rishabh@agentr.dev",
        "List last 3 email in my inbox. use user_id: rishabh@agentr.dev"
    ],
    validate_query = (
        "First, confirm if the email was sent successfully in the first task. "
        "Then, check the emails you just listed and tell me if any of them have the message 'hey what are you upto'. "
        "Answer with 'yes' or 'no' for both parts, and explain your reasoning."
    )
)


@pytest.mark.asyncio
async def test_outlook_tools():
    """Test Outlook integration with specific tools."""
    await execute_case(outlook_test_case)


if __name__ == "__main__":
    asyncio.run(execute_case(outlook_test_case)) 