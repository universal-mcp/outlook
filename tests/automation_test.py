import pytest
import asyncio

from universal_mcp.utils.testing import (
    AutomationTestCase, 
    execute_automation_test,
    create_app_with_integration
)
from universal_mcp_outlook.app import OutlookApp


@pytest.fixture
def outlook_app():
    return create_app_with_integration("outlook", OutlookApp)


@pytest.fixture
def outlook_test_case(outlook_app):
    return AutomationTestCase(
        app="outlook",
        app_instance=outlook_app,
        tools=["user_send_mail", "user_list_message", "get_user_id"],
        tasks=[
            "Get the user id.",
            "Send an email to rshvraj36@gmail.com saying subject: hello and message: no problem.",
            "List last 3 email in my inbox."
        ],
        validate_query = (
            "First, confirm if the user id is correct in the first task. "
            "Then, confirm if the email was sent successfully in the second task. "
            "Then, check the emails you just listed and tell me if any of them have the message 'no problem'. "
            "Answer in JSON format with only a 'success' boolean field that is true only if all parts are confirmed."
        )
    )


@pytest.mark.asyncio
async def test_outlook_tools(outlook_test_case):
    """Test Outlook integration with specific tools."""
    await execute_automation_test(outlook_test_case)


 