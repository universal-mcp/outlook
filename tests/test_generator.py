import os
from pydantic import SecretStr, BaseModel
from langchain_openai import AzureChatOpenAI

from universal_mcp_outlook.app import OutlookApp
from universal_mcp.tools import ToolManager
from universal_mcp.tools.adapters import ToolFormat
from langchain_core.messages import SystemMessage, HumanMessage



class TestCaseOutput(BaseModel):
    """Simplified test case for LLM structured output (without app_instance)."""
    tools: list[str]
    tasks: list[str]
    validate_query: str


app = OutlookApp(integration=None)  # type: ignore

def generate_test_case():
    tool_manager = ToolManager()
    tool_manager.register_tools_from_app(app)
    tool_def = tool_manager.list_tools(format=ToolFormat.OPENAI)
    
    # Create system and user prompts
    system_prompt = """You are an expert QA Developer experienced in writing comprehensive test cases for an application.

CORE PRINCIPLES:
- Generate test cases that thoroughly validate application functionality
- Ensure complete coverage of available tools and their capabilities
- Create realistic scenarios that mirror actual user workflows
- Always include proper validation mechanisms

MANDATORY RULES:
1. TOOL DEPENDENCY MANAGEMENT:
   - Always maintain tool dependency relationships
   - Ensure all available tools are covered across test cases
   - Verify tool prerequisites are met before usage
   - Include fallback scenarios for tool failures

2. CRUD OPERATIONS COVERAGE:
   - Analyze available tools to identify CRUD capabilities
   - CREATE: If create/send/compose tools are available, include operations that create new items
   - READ: If list/get/retrieve tools are available, include operations that fetch and display information
   - UPDATE: If update/edit/modify tools are available, include operations that modify existing items
   - DELETE: If delete/remove tools are available, include operations that remove items
   - DEPENDENCY MANAGEMENT: For operations that require prerequisites:
     * To DELETE an email: Must first CREATE it, then READ to verify existence, then DELETE
     * To UPDATE an item: Must first CREATE it, then READ to verify, then UPDATE
     * To READ specific items: May need to CREATE them first if they don't exist
   - Only include CRUD operations that are supported by the available tools
   - Create logical workflows that respect CRUD dependencies (CREATE → READ → UPDATE → DELETE)

3. VALIDATION REQUIREMENTS:
   - Write detailed validation queries for every test case
   - Include both positive and negative validation scenarios
   - Verify data integrity after each operation
   - Check for proper error handling and edge cases

4. FORMATTING STANDARDS:
   - Use single quotes for nested quotes (e.g., "Send email to 'user@example.com' with subject 'Hello'")
   - Structure tasks in logical sequential order
   - Include clear, actionable step descriptions
   - Ensure validation queries are specific and measurable



EXAMPLE TEST CASE STRUCTURE:
- For Outlook Application:
    Tasks:
        1. Get the user ID and verify login status
        2. Send an email to 'test@example.com' with subject 'Test Subject' and message 'Test Body'
        3. List the last 5 emails in inbox and display their subjects
        4. Mark the first email as read (if update functionality available)
        5. Delete a specific email (if delete functionality available)
    Validation Query:
        Based on the conversation history, verify:
        1. Was user ID retrieved successfully?
        2. Was the email sent successfully with correct recipient, subject, and body?
        3. Were exactly 5 emails listed with proper subject display?
        4. Was the email marked as read correctly (if attempted)?
        5. Was the email deleted successfully (if attempted)?
        6. Are there any error messages or failed operations?
"""

    user_prompt = f"""Generate a comprehensive test case for Outlook application using the available tools.

AVAILABLE TOOLS: {tool_def}

REQUIREMENTS:
Create a detailed test case that includes:

1. TOOL ANALYSIS AND SELECTION:
   - Analyze available tools to identify CRUD capabilities
   - Categorize tools by operation type (CREATE, READ, UPDATE, DELETE)
   - Identify tool dependencies and prerequisite relationships
   - Select tools that enable complete workflows, not just isolated operations
   - If certain CRUD operations are missing, focus on available operations only

2. TASK DESIGN WITH CRUD DEPENDENCIES:
   - Create 5-8 realistic tasks based on available tool capabilities
   - Follow logical CRUD workflows where dependencies exist:
     * Example: CREATE email → READ to verify → UPDATE if possible → DELETE if needed
   - Include only operations supported by available tools
   - Structure tasks in dependency order (prerequisites first)
   - Include error handling for missing dependencies

3. VALIDATION STRATEGY:
   - Write specific validation queries for each task
   - Include success criteria and failure conditions
   - Verify data integrity and consistency
   - Check for proper error messages and handling
   - Validate user experience and interface responses

4. EDGE CASES:
   - Include boundary condition testing
   - Test with invalid inputs or parameters
   - Verify permission and access control scenarios
   - Test system behavior under different conditions

Generate the test case now following these requirements."""
    
    # Setup LLM
    azure_api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    if not azure_api_key:
        raise ValueError("AZURE_OPENAI_API_KEY environment variable is required")
    
    llm = AzureChatOpenAI(
        azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT", "o4-mini"),
        api_key=SecretStr(azure_api_key),
        api_version=os.environ.get("AZURE_OPENAI_API_VERSION", "2025-03-01-preview"),
    )
    
    # Get structured output from LLM using system and user prompts
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    
    structured_llm = llm.with_structured_output(TestCaseOutput)
    response = structured_llm.invoke(messages)
    
    write_to_file(response)  # type: ignore
    
    return response


def write_to_file(test_case: TestCaseOutput):
    """Regenerate the entire automation_test.py file with the test case."""
    
    
    app_name = "outlook"
    app_class = "OutlookApp"
    
    # Format tools array with proper indentation and escape quotes
    tools_formatted = "[\n"
    for tool in test_case.tools:
        # Escape double quotes in the tool string
        escaped_tool = tool.replace('"', '\\"')
        tools_formatted += f'        "{escaped_tool}",\n'
    tools_formatted += "    ]"
    
    # Format tasks array with proper indentation and escape quotes
    tasks_formatted = "[\n"
    for task in test_case.tasks:
        # Escape double quotes in the task string
        escaped_task = task.replace('"', '\\"')
        tasks_formatted += f'        "{escaped_task}",\n'
    tasks_formatted += "    ]"
    
    file_content = f'''import pytest

from universal_mcp.utils.testing import (
    AutomationTestCase, 
    execute_automation_test,
    create_app_with_integration
)
from universal_mcp_{app_name}.app import {app_class}


@pytest.fixture
def {app_name}_app():
    return create_app_with_integration("{app_name}", {app_class})


@pytest.fixture
def {app_name}_test_case({app_name}_app):
    return AutomationTestCase(
        app="{app_name}",
        app_instance={app_name}_app,
        tools={tools_formatted},
        tasks={tasks_formatted},
        validate_query = (
            "{test_case.validate_query.replace('"', '\\"')}"
        )
    )


@pytest.mark.asyncio
async def test_{app_name}_tools({app_name}_test_case):
    await execute_automation_test({app_name}_test_case)


 '''
    
    # Write the entire file
    with open("tests/automation_test.py", "w") as f:
        f.write(file_content)
    
    print(f"✅ Generated entire automation_test.py file for {app_name}")


if __name__ == "__main__":
    generate_test_case()