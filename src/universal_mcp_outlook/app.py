from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
from universal_mcp_outlook.api_segments.users_api_mail import UsersApiMail
from universal_mcp_outlook.api_segments.users_api_calender import UsersApiCalender
from universal_mcp_outlook.api_segments.groups_api import GroupsApi
from universal_mcp_outlook.api_segments.places_api import PlacesApi

class OutlookApp(APIApplication):

    def __init__(self, integration: Integration=None, **kwargs) -> None:
        super().__init__(name='outlookapp', integration=integration, **kwargs)
        self.base_url = 'https://graph.microsoft.com/v1.0'
        self.users_mail = UsersApiMail(self)
        self.users_calender = UsersApiCalender(self)
        self.groups = GroupsApi(self)
        self.places = PlacesApi(self)

    def list_tools(self):
        all_tools = []
        all_tools.extend(self.users_mail.list_tools())
        all_tools.extend(self.users_calender.list_tools())
        all_tools.extend(self.groups.list_tools())
        all_tools.extend(self.places.list_tools())
        return all_tools