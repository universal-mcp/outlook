from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
from universal_mcp_outlook.api_segments.users_api import UsersApi

class OutlookApp(APIApplication):

    def __init__(self, integration: Integration=None, **kwargs) -> None:
        super().__init__(name='outlookapp', integration=integration, **kwargs)
        self.base_url = 'https://graph.microsoft.com/v1.0'
        self.users = UsersApi(self)

    def list_tools(self):
        all_tools = []
        all_tools.extend(self.users.list_tools())
        return all_tools