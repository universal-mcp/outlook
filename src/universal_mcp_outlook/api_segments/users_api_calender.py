from typing import Any, List, Optional
from .api_segment_base import APISegmentBase


class UsersApiCalender(APISegmentBase):

    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def user_get_calendar(
        self,
        user_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_update_calendar(
        self,
        user_id: str,
        id: Optional[str] = None,
        allowedOnlineMeetingProviders: Optional[List[str]] = None,
        canEdit: Optional[bool] = None,
        canShare: Optional[bool] = None,
        canViewPrivateItems: Optional[bool] = None,
        changeKey: Optional[str] = None,
        color: Optional[str] = None,
        defaultOnlineMeetingProvider: Optional[str] = None,
        hexColor: Optional[str] = None,
        isDefaultCalendar: Optional[bool] = None,
        isRemovable: Optional[bool] = None,
        isTallyingResponses: Optional[bool] = None,
        name: Optional[str] = None,
        owner: Optional[dict[str, dict[str, Any]]] = None,
        calendarPermissions: Optional[List[Any]] = None,
        calendarView: Optional[List[Any]] = None,
        events: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property calendar in users

        Args:
            user_id (string): user-id
            id (string): The unique identifier for an entity. Read-only.
            allowedOnlineMeetingProviders (array): Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
            canEdit (boolean): true if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who shared a calendar and granted write access.
            canShare (boolean): true if the user has permission to share the calendar, false otherwise. Only the user who created the calendar can share it.
            canViewPrivateItems (boolean): If true, the user can read calendar items that have been marked private, false otherwise.
            changeKey (string): Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            color (string): color
            defaultOnlineMeetingProvider (string): defaultOnlineMeetingProvider
            hexColor (string): The calendar color, expressed in a hex color code of three hexadecimal values, each ranging from 00 to FF and representing the red, green, or blue components of the color in the RGB color space. If the user has never explicitly set a color for the calendar, this property is empty. Read-only.
            isDefaultCalendar (boolean): true if this is the default calendar where new events are created by default, false otherwise.
            isRemovable (boolean): Indicates whether this user calendar can be deleted from the user mailbox.
            isTallyingResponses (boolean): Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.
            name (string): The calendar name.
            owner (object): owner
            calendarPermissions (array): The permissions of the users with whom the calendar is shared.
            calendarView (array): The calendar view for the calendar. Navigation property. Read-only.
            events (array): The events in the calendar. Navigation property. Read-only.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the calendar. Read-only. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "allowedOnlineMeetingProviders": allowedOnlineMeetingProviders,
            "canEdit": canEdit,
            "canShare": canShare,
            "canViewPrivateItems": canViewPrivateItems,
            "changeKey": changeKey,
            "color": color,
            "defaultOnlineMeetingProvider": defaultOnlineMeetingProvider,
            "hexColor": hexColor,
            "isDefaultCalendar": isDefaultCalendar,
            "isRemovable": isRemovable,
            "isTallyingResponses": isTallyingResponses,
            "name": name,
            "owner": owner,
            "calendarPermissions": calendarPermissions,
            "calendarView": calendarView,
            "events": events,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_list_calendar_permission(
        self,
        user_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        List calendarPermissions

        Args:
            user_id (string): user-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarPermissions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_create_calendar_permission(
        self,
        user_id: str,
        id: Optional[str] = None,
        allowedRoles: Optional[List[str]] = None,
        emailAddress: Optional[dict[str, dict[str, Any]]] = None,
        isInsideOrganization: Optional[bool] = None,
        isRemovable: Optional[bool] = None,
        role: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to calendarPermissions for users

        Args:
            user_id (string): user-id
            id (string): The unique identifier for an entity. Read-only.
            allowedRoles (array): List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.
            emailAddress (object): emailAddress
            isInsideOrganization (boolean): True if the user in context (recipient or delegate) is inside the same organization as the calendar owner.
            isRemovable (boolean): True if the user can be removed from the list of recipients or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You can't remove 'My organization' as a share recipient to a calendar.
            role (string): role

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "allowedRoles": allowedRoles,
            "emailAddress": emailAddress,
            "isInsideOrganization": isInsideOrganization,
            "isRemovable": isRemovable,
            "role": role,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarPermissions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_get_calendar_permission(
        self,
        user_id: str,
        calendarPermission_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendarPermission

        Args:
            user_id (string): user-id
            calendarPermission_id (string): calendarPermission-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarPermission_id is None:
            raise ValueError("Missing required parameter 'calendarPermission-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarPermissions/{calendarPermission_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_update_calendar_permission(
        self,
        user_id: str,
        calendarPermission_id: str,
        id: Optional[str] = None,
        allowedRoles: Optional[List[str]] = None,
        emailAddress: Optional[dict[str, dict[str, Any]]] = None,
        isInsideOrganization: Optional[bool] = None,
        isRemovable: Optional[bool] = None,
        role: Optional[str] = None,
    ) -> Any:
        """

        Update calendarPermission

        Args:
            user_id (string): user-id
            calendarPermission_id (string): calendarPermission-id
            id (string): The unique identifier for an entity. Read-only.
            allowedRoles (array): List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.
            emailAddress (object): emailAddress
            isInsideOrganization (boolean): True if the user in context (recipient or delegate) is inside the same organization as the calendar owner.
            isRemovable (boolean): True if the user can be removed from the list of recipients or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You can't remove 'My organization' as a share recipient to a calendar.
            role (string): role

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarPermission_id is None:
            raise ValueError("Missing required parameter 'calendarPermission-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "allowedRoles": allowedRoles,
            "emailAddress": emailAddress,
            "isInsideOrganization": isInsideOrganization,
            "isRemovable": isRemovable,
            "role": role,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarPermissions/{calendarPermission_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_delete_calendar_permission(
        self, user_id: str, calendarPermission_id: str
    ) -> Any:
        """

        Delete calendarPermission

        Args:
            user_id (string): user-id
            calendarPermission_id (string): calendarPermission-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarPermission_id is None:
            raise ValueError("Missing required parameter 'calendarPermission-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarPermissions/{calendarPermission_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_permission_get_count(
        self, user_id: str, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarPermissions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_list_calendar_view(
        self,
        user_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get calendarView from users

        Args:
            user_id (string): user-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_get_calendar_view(
        self,
        user_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendarView from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_list_attachment(
        self,
        user_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_create_attachment(
        self,
        user_id: str,
        event_id: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_get_attachment(
        self,
        user_id: str,
        event_id: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_delete_attachment(
        self, user_id: str, event_id: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_attachment_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_attachment_create_upload_session(
        self,
        user_id: str,
        event_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            event_id (string): event-id
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_get_calendar(
        self,
        user_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_list_extension(
        self,
        user_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_create_extension(
        self, user_id: str, event_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_get_extension(
        self,
        user_id: str,
        event_id: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_update_extension(
        self, user_id: str, event_id: str, extension_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_delete_extension(
        self, user_id: str, event_id: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_extension_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_list_instance(
        self,
        user_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_get_instance(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_list_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_create_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_get_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_delete_attachment(
        self, user_id: str, event_id: str, event_id1: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_attachment_get_count(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_attachment_create_upload_session(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_get_calendar(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_list_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_create_extension(
        self, user_id: str, event_id: str, event_id1: str, id: Optional[str] = None
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_get_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_update_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_delete_extension(
        self, user_id: str, event_id: str, event_id1: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_extension_get_count(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_accept(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_cancel(
        self, user_id: str, event_id: str, event_id1: str, Comment: Optional[str] = None
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_decline(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_dismiss_reminder(
        self, user_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_forward(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_permanent_delete(
        self, user_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_snooze_reminder(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_tentatively_accept(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_delta(
        self,
        user_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/instances/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_accept(
        self,
        user_id: str,
        event_id: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_cancel(
        self, user_id: str, event_id: str, Comment: Optional[str] = None
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            event_id (string): event-id
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_decline(
        self,
        user_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_dismiss_reminder(
        self, user_id: str, event_id: str
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_forward(
        self,
        user_id: str,
        event_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_permanent_delete(
        self, user_id: str, event_id: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_snooze_reminder(
        self,
        user_id: str,
        event_id: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_tentatively_accept(
        self,
        user_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/{event_id}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_get_count(
        self, user_id: str, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_delta(
        self,
        user_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/calendarView/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_list_event(
        self,
        user_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get events from users

        Args:
            user_id (string): user-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_create_event(
        self,
        user_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        allowNewTimeProposals: Optional[bool] = None,
        attendees: Optional[List[Any]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        end: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        hideAttendees: Optional[bool] = None,
        iCalUId: Optional[str] = None,
        importance: Optional[str] = None,
        isAllDay: Optional[bool] = None,
        isCancelled: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isOnlineMeeting: Optional[bool] = None,
        isOrganizer: Optional[bool] = None,
        isReminderOn: Optional[bool] = None,
        location: Optional[dict[str, dict[str, Any]]] = None,
        locations: Optional[List[dict[str, dict[str, Any]]]] = None,
        onlineMeeting: Optional[dict[str, dict[str, Any]]] = None,
        onlineMeetingProvider: Optional[str] = None,
        onlineMeetingUrl: Optional[str] = None,
        organizer: Optional[dict[str, dict[str, Any]]] = None,
        originalEndTimeZone: Optional[str] = None,
        originalStart: Optional[str] = None,
        originalStartTimeZone: Optional[str] = None,
        recurrence: Optional[dict[str, dict[str, Any]]] = None,
        reminderMinutesBeforeStart: Optional[float] = None,
        responseRequested: Optional[bool] = None,
        responseStatus: Optional[dict[str, dict[str, Any]]] = None,
        sensitivity: Optional[str] = None,
        seriesMasterId: Optional[str] = None,
        showAs: Optional[str] = None,
        start: Optional[dict[str, dict[str, Any]]] = None,
        subject: Optional[str] = None,
        transactionId: Optional[str] = None,
        type: Optional[str] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        calendar: Optional[Any] = None,
        extensions: Optional[List[Any]] = None,
        instances: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to events for users

        Args:
            user_id (string): user-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            allowNewTimeProposals (boolean): true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. The default is true.
            attendees (array): The collection of attendees for the event.
            body (object): body
            bodyPreview (string): The preview of the message associated with the event. It's in text format.
            end (object): end
            hasAttachments (boolean): Set to true if the event has attachments.
            hideAttendees (boolean): When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. The default is false.
            iCalUId (string): A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
            importance (string): importance
            isAllDay (boolean): Set to true if the event lasts all day. If true, regardless of whether it's a single-day or multi-day event, start, and endtime must be set to midnight and be in the same time zone.
            isCancelled (boolean): Set to true if the event has been canceled.
            isDraft (boolean): Set to true if the user has updated the meeting in Outlook but hasn't sent the updates to attendees. Set to false if all changes are sent, or if the event is an appointment without any attendees.
            isOnlineMeeting (boolean): True if this event has online meeting information (that is, onlineMeeting points to an onlineMeetingInfo resource), false otherwise. Default is false (onlineMeeting is null). Optional.  After you set isOnlineMeeting to true, Microsoft Graph initializes onlineMeeting. Subsequently, Outlook ignores any further changes to isOnlineMeeting, and the meeting remains available online.
            isOrganizer (boolean): Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). It also applies if a delegate organized the event on behalf of the owner.
            isReminderOn (boolean): Set to true if an alert is set to remind the user of the event.
            location (object): location
            locations (array): The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection are removed and replaced by the new location value.
            onlineMeeting (object): onlineMeeting
            onlineMeetingProvider (string): onlineMeetingProvider
            onlineMeetingUrl (string): A URL for an online meeting. The property is set only when an organizer specifies in Outlook that an event is an online meeting such as Skype. Read-only.To access the URL to join an online meeting, use joinUrl which is exposed via the onlineMeeting property of the event. The onlineMeetingUrl property will be deprecated in the future.
            organizer (object): organizer
            originalEndTimeZone (string): The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            originalStart (string): Represents the start time of an event when it's initially created as an occurrence or exception in a recurring series. This property is not returned for events that are single instances. Its date and time information is expressed in ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            originalStartTimeZone (string): The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            recurrence (object): recurrence
            reminderMinutesBeforeStart (number): The number of minutes before the event start time that the reminder alert occurs.
            responseRequested (boolean): Default is true, which represents the organizer would like an invitee to send a response to the event.
            responseStatus (object): responseStatus
            sensitivity (string): sensitivity
            seriesMasterId (string): The ID for the recurring series master item, if this event is part of a recurring series.
            showAs (string): showAs
            start (object): start
            subject (string): The text of the event's subject line.
            transactionId (string): A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. It's useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you can't change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.
            type (string): type
            webLink (string): The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can't be accessed from within an iFrame.
            attachments (array): The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
            calendar (string): calendar
            extensions (array): The collection of open extensions defined for the event. Nullable.
            instances (array): The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions modified, but doesn't include occurrences cancelled from the series. Navigation property. Read-only. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the event. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the event. Read-only. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "allowNewTimeProposals": allowNewTimeProposals,
            "attendees": attendees,
            "body": body,
            "bodyPreview": bodyPreview,
            "end": end,
            "hasAttachments": hasAttachments,
            "hideAttendees": hideAttendees,
            "iCalUId": iCalUId,
            "importance": importance,
            "isAllDay": isAllDay,
            "isCancelled": isCancelled,
            "isDraft": isDraft,
            "isOnlineMeeting": isOnlineMeeting,
            "isOrganizer": isOrganizer,
            "isReminderOn": isReminderOn,
            "location": location,
            "locations": locations,
            "onlineMeeting": onlineMeeting,
            "onlineMeetingProvider": onlineMeetingProvider,
            "onlineMeetingUrl": onlineMeetingUrl,
            "organizer": organizer,
            "originalEndTimeZone": originalEndTimeZone,
            "originalStart": originalStart,
            "originalStartTimeZone": originalStartTimeZone,
            "recurrence": recurrence,
            "reminderMinutesBeforeStart": reminderMinutesBeforeStart,
            "responseRequested": responseRequested,
            "responseStatus": responseStatus,
            "sensitivity": sensitivity,
            "seriesMasterId": seriesMasterId,
            "showAs": showAs,
            "start": start,
            "subject": subject,
            "transactionId": transactionId,
            "type": type,
            "webLink": webLink,
            "attachments": attachments,
            "calendar": calendar,
            "extensions": extensions,
            "instances": instances,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_get_event(
        self,
        user_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get events from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_update_event(
        self,
        user_id: str,
        event_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        allowNewTimeProposals: Optional[bool] = None,
        attendees: Optional[List[Any]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        end: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        hideAttendees: Optional[bool] = None,
        iCalUId: Optional[str] = None,
        importance: Optional[str] = None,
        isAllDay: Optional[bool] = None,
        isCancelled: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isOnlineMeeting: Optional[bool] = None,
        isOrganizer: Optional[bool] = None,
        isReminderOn: Optional[bool] = None,
        location: Optional[dict[str, dict[str, Any]]] = None,
        locations: Optional[List[dict[str, dict[str, Any]]]] = None,
        onlineMeeting: Optional[dict[str, dict[str, Any]]] = None,
        onlineMeetingProvider: Optional[str] = None,
        onlineMeetingUrl: Optional[str] = None,
        organizer: Optional[dict[str, dict[str, Any]]] = None,
        originalEndTimeZone: Optional[str] = None,
        originalStart: Optional[str] = None,
        originalStartTimeZone: Optional[str] = None,
        recurrence: Optional[dict[str, dict[str, Any]]] = None,
        reminderMinutesBeforeStart: Optional[float] = None,
        responseRequested: Optional[bool] = None,
        responseStatus: Optional[dict[str, dict[str, Any]]] = None,
        sensitivity: Optional[str] = None,
        seriesMasterId: Optional[str] = None,
        showAs: Optional[str] = None,
        start: Optional[dict[str, dict[str, Any]]] = None,
        subject: Optional[str] = None,
        transactionId: Optional[str] = None,
        type: Optional[str] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        calendar: Optional[Any] = None,
        extensions: Optional[List[Any]] = None,
        instances: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property events in users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            allowNewTimeProposals (boolean): true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. The default is true.
            attendees (array): The collection of attendees for the event.
            body (object): body
            bodyPreview (string): The preview of the message associated with the event. It's in text format.
            end (object): end
            hasAttachments (boolean): Set to true if the event has attachments.
            hideAttendees (boolean): When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. The default is false.
            iCalUId (string): A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
            importance (string): importance
            isAllDay (boolean): Set to true if the event lasts all day. If true, regardless of whether it's a single-day or multi-day event, start, and endtime must be set to midnight and be in the same time zone.
            isCancelled (boolean): Set to true if the event has been canceled.
            isDraft (boolean): Set to true if the user has updated the meeting in Outlook but hasn't sent the updates to attendees. Set to false if all changes are sent, or if the event is an appointment without any attendees.
            isOnlineMeeting (boolean): True if this event has online meeting information (that is, onlineMeeting points to an onlineMeetingInfo resource), false otherwise. Default is false (onlineMeeting is null). Optional.  After you set isOnlineMeeting to true, Microsoft Graph initializes onlineMeeting. Subsequently, Outlook ignores any further changes to isOnlineMeeting, and the meeting remains available online.
            isOrganizer (boolean): Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). It also applies if a delegate organized the event on behalf of the owner.
            isReminderOn (boolean): Set to true if an alert is set to remind the user of the event.
            location (object): location
            locations (array): The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection are removed and replaced by the new location value.
            onlineMeeting (object): onlineMeeting
            onlineMeetingProvider (string): onlineMeetingProvider
            onlineMeetingUrl (string): A URL for an online meeting. The property is set only when an organizer specifies in Outlook that an event is an online meeting such as Skype. Read-only.To access the URL to join an online meeting, use joinUrl which is exposed via the onlineMeeting property of the event. The onlineMeetingUrl property will be deprecated in the future.
            organizer (object): organizer
            originalEndTimeZone (string): The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            originalStart (string): Represents the start time of an event when it's initially created as an occurrence or exception in a recurring series. This property is not returned for events that are single instances. Its date and time information is expressed in ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            originalStartTimeZone (string): The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            recurrence (object): recurrence
            reminderMinutesBeforeStart (number): The number of minutes before the event start time that the reminder alert occurs.
            responseRequested (boolean): Default is true, which represents the organizer would like an invitee to send a response to the event.
            responseStatus (object): responseStatus
            sensitivity (string): sensitivity
            seriesMasterId (string): The ID for the recurring series master item, if this event is part of a recurring series.
            showAs (string): showAs
            start (object): start
            subject (string): The text of the event's subject line.
            transactionId (string): A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. It's useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you can't change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.
            type (string): type
            webLink (string): The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can't be accessed from within an iFrame.
            attachments (array): The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
            calendar (string): calendar
            extensions (array): The collection of open extensions defined for the event. Nullable.
            instances (array): The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions modified, but doesn't include occurrences cancelled from the series. Navigation property. Read-only. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the event. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the event. Read-only. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "allowNewTimeProposals": allowNewTimeProposals,
            "attendees": attendees,
            "body": body,
            "bodyPreview": bodyPreview,
            "end": end,
            "hasAttachments": hasAttachments,
            "hideAttendees": hideAttendees,
            "iCalUId": iCalUId,
            "importance": importance,
            "isAllDay": isAllDay,
            "isCancelled": isCancelled,
            "isDraft": isDraft,
            "isOnlineMeeting": isOnlineMeeting,
            "isOrganizer": isOrganizer,
            "isReminderOn": isReminderOn,
            "location": location,
            "locations": locations,
            "onlineMeeting": onlineMeeting,
            "onlineMeetingProvider": onlineMeetingProvider,
            "onlineMeetingUrl": onlineMeetingUrl,
            "organizer": organizer,
            "originalEndTimeZone": originalEndTimeZone,
            "originalStart": originalStart,
            "originalStartTimeZone": originalStartTimeZone,
            "recurrence": recurrence,
            "reminderMinutesBeforeStart": reminderMinutesBeforeStart,
            "responseRequested": responseRequested,
            "responseStatus": responseStatus,
            "sensitivity": sensitivity,
            "seriesMasterId": seriesMasterId,
            "showAs": showAs,
            "start": start,
            "subject": subject,
            "transactionId": transactionId,
            "type": type,
            "webLink": webLink,
            "attachments": attachments,
            "calendar": calendar,
            "extensions": extensions,
            "instances": instances,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_delete_event(self, user_id: str, event_id: str) -> Any:
        """

        Delete navigation property events for users

        Args:
            user_id (string): user-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_list_attachment(
        self,
        user_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_create_attachment(
        self,
        user_id: str,
        event_id: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_get_attachment(
        self,
        user_id: str,
        event_id: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_delete_attachment(
        self, user_id: str, event_id: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_attachment_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_attachment_create_upload_session(
        self,
        user_id: str,
        event_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            event_id (string): event-id
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_get_calendar(
        self,
        user_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_list_extension(
        self,
        user_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_create_extension(
        self, user_id: str, event_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_get_extension(
        self,
        user_id: str,
        event_id: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_update_extension(
        self, user_id: str, event_id: str, extension_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_delete_extension(
        self, user_id: str, event_id: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_extension_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_list_instance(
        self,
        user_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_get_instance(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_list_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_create_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_get_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_delete_attachment(
        self, user_id: str, event_id: str, event_id1: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_attachment_get_count(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_attachment_create_upload_session(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_get_calendar(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_list_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_create_extension(
        self, user_id: str, event_id: str, event_id1: str, id: Optional[str] = None
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_get_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_update_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_delete_extension(
        self, user_id: str, event_id: str, event_id1: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_extension_get_count(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_accept(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_cancel(
        self, user_id: str, event_id: str, event_id1: str, Comment: Optional[str] = None
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_decline(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_dismiss_reminder(
        self, user_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_forward(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_permanent_delete(
        self, user_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_snooze_reminder(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_tentatively_accept(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/{event_id1}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_delta(
        self,
        user_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/instances/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_accept(
        self,
        user_id: str,
        event_id: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_cancel(
        self, user_id: str, event_id: str, Comment: Optional[str] = None
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            event_id (string): event-id
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_decline(
        self,
        user_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_dismiss_reminder(self, user_id: str, event_id: str) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_forward(
        self,
        user_id: str,
        event_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_permanent_delete(self, user_id: str, event_id: str) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_snooze_reminder(
        self,
        user_id: str,
        event_id: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_tentatively_accept(
        self,
        user_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/{event_id}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_get_count(
        self, user_id: str, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_delta(
        self,
        user_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/events/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_allowed_calendar_sharing_role(
        self,
        user_id: str,
        User: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
    ) -> dict[str, Any]:
        """

        Invoke function allowedCalendarSharingRoles

        Args:
            user_id (string): user-id
            User (string): User
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if User is None:
            raise ValueError("Missing required parameter 'User'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/microsoft.graph.allowedCalendarSharingRoles(User='{User}')"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_get_schedule(
        self,
        user_id: str,
        Schedules: Optional[List[str]] = None,
        EndTime: Optional[dict[str, dict[str, Any]]] = None,
        StartTime: Optional[dict[str, dict[str, Any]]] = None,
        AvailabilityViewInterval: Optional[float] = None,
    ) -> dict[str, Any]:
        """

        Invoke action getSchedule

        Args:
            user_id (string): user-id
            Schedules (array): Schedules
            EndTime (object): EndTime
            StartTime (object): StartTime
            AvailabilityViewInterval (number): AvailabilityViewInterval

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        request_body_data = None
        request_body_data = {
            "Schedules": Schedules,
            "EndTime": EndTime,
            "StartTime": StartTime,
            "AvailabilityViewInterval": AvailabilityViewInterval,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/microsoft.graph.getSchedule"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_permanent_delete(self, user_id: str) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendar/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_list_calendar_group(
        self,
        user_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get calendarGroups from users

        Args:
            user_id (string): user-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_create_calendar_group(
        self,
        user_id: str,
        id: Optional[str] = None,
        changeKey: Optional[str] = None,
        classId: Optional[str] = None,
        name: Optional[str] = None,
        calendars: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to calendarGroups for users

        Args:
            user_id (string): user-id
            id (string): The unique identifier for an entity. Read-only.
            changeKey (string): Identifies the version of the calendar group. Every time the calendar group is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            classId (string): The class identifier. Read-only.
            name (string): The group name.
            calendars (array): The calendars in the calendar group. Navigation property. Read-only. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "changeKey": changeKey,
            "classId": classId,
            "name": name,
            "calendars": calendars,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_get_calendar_group(
        self,
        user_id: str,
        calendarGroup_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendarGroups from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_update_calendar_group(
        self,
        user_id: str,
        calendarGroup_id: str,
        id: Optional[str] = None,
        changeKey: Optional[str] = None,
        classId: Optional[str] = None,
        name: Optional[str] = None,
        calendars: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property calendarGroups in users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            id (string): The unique identifier for an entity. Read-only.
            changeKey (string): Identifies the version of the calendar group. Every time the calendar group is changed, ChangeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            classId (string): The class identifier. Read-only.
            name (string): The group name.
            calendars (array): The calendars in the calendar group. Navigation property. Read-only. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "changeKey": changeKey,
            "classId": classId,
            "name": name,
            "calendars": calendars,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_delete_calendar_group(self, user_id: str, calendarGroup_id: str) -> Any:
        """

        Delete navigation property calendarGroups for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_list_calendar(
        self,
        user_id: str,
        calendarGroup_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get calendars from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_create_calendar(
        self,
        user_id: str,
        calendarGroup_id: str,
        id: Optional[str] = None,
        allowedOnlineMeetingProviders: Optional[List[str]] = None,
        canEdit: Optional[bool] = None,
        canShare: Optional[bool] = None,
        canViewPrivateItems: Optional[bool] = None,
        changeKey: Optional[str] = None,
        color: Optional[str] = None,
        defaultOnlineMeetingProvider: Optional[str] = None,
        hexColor: Optional[str] = None,
        isDefaultCalendar: Optional[bool] = None,
        isRemovable: Optional[bool] = None,
        isTallyingResponses: Optional[bool] = None,
        name: Optional[str] = None,
        owner: Optional[dict[str, dict[str, Any]]] = None,
        calendarPermissions: Optional[List[Any]] = None,
        calendarView: Optional[List[Any]] = None,
        events: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to calendars for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            id (string): The unique identifier for an entity. Read-only.
            allowedOnlineMeetingProviders (array): Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
            canEdit (boolean): true if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who shared a calendar and granted write access.
            canShare (boolean): true if the user has permission to share the calendar, false otherwise. Only the user who created the calendar can share it.
            canViewPrivateItems (boolean): If true, the user can read calendar items that have been marked private, false otherwise.
            changeKey (string): Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            color (string): color
            defaultOnlineMeetingProvider (string): defaultOnlineMeetingProvider
            hexColor (string): The calendar color, expressed in a hex color code of three hexadecimal values, each ranging from 00 to FF and representing the red, green, or blue components of the color in the RGB color space. If the user has never explicitly set a color for the calendar, this property is empty. Read-only.
            isDefaultCalendar (boolean): true if this is the default calendar where new events are created by default, false otherwise.
            isRemovable (boolean): Indicates whether this user calendar can be deleted from the user mailbox.
            isTallyingResponses (boolean): Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.
            name (string): The calendar name.
            owner (object): owner
            calendarPermissions (array): The permissions of the users with whom the calendar is shared.
            calendarView (array): The calendar view for the calendar. Navigation property. Read-only.
            events (array): The events in the calendar. Navigation property. Read-only.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the calendar. Read-only. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "allowedOnlineMeetingProviders": allowedOnlineMeetingProviders,
            "canEdit": canEdit,
            "canShare": canShare,
            "canViewPrivateItems": canViewPrivateItems,
            "changeKey": changeKey,
            "color": color,
            "defaultOnlineMeetingProvider": defaultOnlineMeetingProvider,
            "hexColor": hexColor,
            "isDefaultCalendar": isDefaultCalendar,
            "isRemovable": isRemovable,
            "isTallyingResponses": isTallyingResponses,
            "name": name,
            "owner": owner,
            "calendarPermissions": calendarPermissions,
            "calendarView": calendarView,
            "events": events,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_get_calendar(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendars from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_update_calendar(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        id: Optional[str] = None,
        allowedOnlineMeetingProviders: Optional[List[str]] = None,
        canEdit: Optional[bool] = None,
        canShare: Optional[bool] = None,
        canViewPrivateItems: Optional[bool] = None,
        changeKey: Optional[str] = None,
        color: Optional[str] = None,
        defaultOnlineMeetingProvider: Optional[str] = None,
        hexColor: Optional[str] = None,
        isDefaultCalendar: Optional[bool] = None,
        isRemovable: Optional[bool] = None,
        isTallyingResponses: Optional[bool] = None,
        name: Optional[str] = None,
        owner: Optional[dict[str, dict[str, Any]]] = None,
        calendarPermissions: Optional[List[Any]] = None,
        calendarView: Optional[List[Any]] = None,
        events: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property calendars in users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            id (string): The unique identifier for an entity. Read-only.
            allowedOnlineMeetingProviders (array): Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
            canEdit (boolean): true if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who shared a calendar and granted write access.
            canShare (boolean): true if the user has permission to share the calendar, false otherwise. Only the user who created the calendar can share it.
            canViewPrivateItems (boolean): If true, the user can read calendar items that have been marked private, false otherwise.
            changeKey (string): Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            color (string): color
            defaultOnlineMeetingProvider (string): defaultOnlineMeetingProvider
            hexColor (string): The calendar color, expressed in a hex color code of three hexadecimal values, each ranging from 00 to FF and representing the red, green, or blue components of the color in the RGB color space. If the user has never explicitly set a color for the calendar, this property is empty. Read-only.
            isDefaultCalendar (boolean): true if this is the default calendar where new events are created by default, false otherwise.
            isRemovable (boolean): Indicates whether this user calendar can be deleted from the user mailbox.
            isTallyingResponses (boolean): Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.
            name (string): The calendar name.
            owner (object): owner
            calendarPermissions (array): The permissions of the users with whom the calendar is shared.
            calendarView (array): The calendar view for the calendar. Navigation property. Read-only.
            events (array): The events in the calendar. Navigation property. Read-only.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the calendar. Read-only. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "allowedOnlineMeetingProviders": allowedOnlineMeetingProviders,
            "canEdit": canEdit,
            "canShare": canShare,
            "canViewPrivateItems": canViewPrivateItems,
            "changeKey": changeKey,
            "color": color,
            "defaultOnlineMeetingProvider": defaultOnlineMeetingProvider,
            "hexColor": hexColor,
            "isDefaultCalendar": isDefaultCalendar,
            "isRemovable": isRemovable,
            "isTallyingResponses": isTallyingResponses,
            "name": name,
            "owner": owner,
            "calendarPermissions": calendarPermissions,
            "calendarView": calendarView,
            "events": events,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_delete_calendar(
        self, user_id: str, calendarGroup_id: str, calendar_id: str
    ) -> Any:
        """

        Delete navigation property calendars for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_list_calendar_permission(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get calendarPermissions from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarPermissions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_create_calendar_permission(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        id: Optional[str] = None,
        allowedRoles: Optional[List[str]] = None,
        emailAddress: Optional[dict[str, dict[str, Any]]] = None,
        isInsideOrganization: Optional[bool] = None,
        isRemovable: Optional[bool] = None,
        role: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to calendarPermissions for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            id (string): The unique identifier for an entity. Read-only.
            allowedRoles (array): List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.
            emailAddress (object): emailAddress
            isInsideOrganization (boolean): True if the user in context (recipient or delegate) is inside the same organization as the calendar owner.
            isRemovable (boolean): True if the user can be removed from the list of recipients or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You can't remove 'My organization' as a share recipient to a calendar.
            role (string): role

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "allowedRoles": allowedRoles,
            "emailAddress": emailAddress,
            "isInsideOrganization": isInsideOrganization,
            "isRemovable": isRemovable,
            "role": role,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarPermissions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_get_calendar_permission(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        calendarPermission_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendarPermissions from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            calendarPermission_id (string): calendarPermission-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if calendarPermission_id is None:
            raise ValueError("Missing required parameter 'calendarPermission-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarPermissions/{calendarPermission_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_update_calendar_permission(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        calendarPermission_id: str,
        id: Optional[str] = None,
        allowedRoles: Optional[List[str]] = None,
        emailAddress: Optional[dict[str, dict[str, Any]]] = None,
        isInsideOrganization: Optional[bool] = None,
        isRemovable: Optional[bool] = None,
        role: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property calendarPermissions in users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            calendarPermission_id (string): calendarPermission-id
            id (string): The unique identifier for an entity. Read-only.
            allowedRoles (array): List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.
            emailAddress (object): emailAddress
            isInsideOrganization (boolean): True if the user in context (recipient or delegate) is inside the same organization as the calendar owner.
            isRemovable (boolean): True if the user can be removed from the list of recipients or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You can't remove 'My organization' as a share recipient to a calendar.
            role (string): role

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if calendarPermission_id is None:
            raise ValueError("Missing required parameter 'calendarPermission-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "allowedRoles": allowedRoles,
            "emailAddress": emailAddress,
            "isInsideOrganization": isInsideOrganization,
            "isRemovable": isRemovable,
            "role": role,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarPermissions/{calendarPermission_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_delete_calendar_permission(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        calendarPermission_id: str,
    ) -> Any:
        """

        Delete navigation property calendarPermissions for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            calendarPermission_id (string): calendarPermission-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if calendarPermission_id is None:
            raise ValueError("Missing required parameter 'calendarPermission-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarPermissions/{calendarPermission_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_permission_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarPermissions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_list_calendar_view(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get calendarView from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_get_calendar_view(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendarView from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_list_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_create_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_get_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_delete_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        attachment_id: str,
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_attachment_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_attachment_create_upload_session(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_get_calendar(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_list_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_create_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_get_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_update_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_delete_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        extension_id: str,
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_extension_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_list_instance(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_get_instance(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_list_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_create_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_get_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_delete_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_attachment_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_attachment_create_upload_session(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_get_calendar(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_list_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_create_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_get_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_update_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_delete_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_extension_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_accept(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_cancel(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_decline(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_dismiss_reminder(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_forward(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_permanent_delete(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_snooze_reminder(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_tentatively_accept(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_instance_delta(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_accept(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_cancel(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_decline(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_dismiss_reminder(
        self, user_id: str, calendarGroup_id: str, calendar_id: str, event_id: str
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_forward(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_permanent_delete(
        self, user_id: str, calendarGroup_id: str, calendar_id: str, event_id: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_snooze_reminder(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_tentatively_accept(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_calendar_view_delta(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/calendarView/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_list_event(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get events from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_create_event(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        allowNewTimeProposals: Optional[bool] = None,
        attendees: Optional[List[Any]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        end: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        hideAttendees: Optional[bool] = None,
        iCalUId: Optional[str] = None,
        importance: Optional[str] = None,
        isAllDay: Optional[bool] = None,
        isCancelled: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isOnlineMeeting: Optional[bool] = None,
        isOrganizer: Optional[bool] = None,
        isReminderOn: Optional[bool] = None,
        location: Optional[dict[str, dict[str, Any]]] = None,
        locations: Optional[List[dict[str, dict[str, Any]]]] = None,
        onlineMeeting: Optional[dict[str, dict[str, Any]]] = None,
        onlineMeetingProvider: Optional[str] = None,
        onlineMeetingUrl: Optional[str] = None,
        organizer: Optional[dict[str, dict[str, Any]]] = None,
        originalEndTimeZone: Optional[str] = None,
        originalStart: Optional[str] = None,
        originalStartTimeZone: Optional[str] = None,
        recurrence: Optional[dict[str, dict[str, Any]]] = None,
        reminderMinutesBeforeStart: Optional[float] = None,
        responseRequested: Optional[bool] = None,
        responseStatus: Optional[dict[str, dict[str, Any]]] = None,
        sensitivity: Optional[str] = None,
        seriesMasterId: Optional[str] = None,
        showAs: Optional[str] = None,
        start: Optional[dict[str, dict[str, Any]]] = None,
        subject: Optional[str] = None,
        transactionId: Optional[str] = None,
        type: Optional[str] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        calendar: Optional[Any] = None,
        extensions: Optional[List[Any]] = None,
        instances: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to events for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            allowNewTimeProposals (boolean): true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. The default is true.
            attendees (array): The collection of attendees for the event.
            body (object): body
            bodyPreview (string): The preview of the message associated with the event. It's in text format.
            end (object): end
            hasAttachments (boolean): Set to true if the event has attachments.
            hideAttendees (boolean): When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. The default is false.
            iCalUId (string): A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
            importance (string): importance
            isAllDay (boolean): Set to true if the event lasts all day. If true, regardless of whether it's a single-day or multi-day event, start, and endtime must be set to midnight and be in the same time zone.
            isCancelled (boolean): Set to true if the event has been canceled.
            isDraft (boolean): Set to true if the user has updated the meeting in Outlook but hasn't sent the updates to attendees. Set to false if all changes are sent, or if the event is an appointment without any attendees.
            isOnlineMeeting (boolean): True if this event has online meeting information (that is, onlineMeeting points to an onlineMeetingInfo resource), false otherwise. Default is false (onlineMeeting is null). Optional.  After you set isOnlineMeeting to true, Microsoft Graph initializes onlineMeeting. Subsequently, Outlook ignores any further changes to isOnlineMeeting, and the meeting remains available online.
            isOrganizer (boolean): Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). It also applies if a delegate organized the event on behalf of the owner.
            isReminderOn (boolean): Set to true if an alert is set to remind the user of the event.
            location (object): location
            locations (array): The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection are removed and replaced by the new location value.
            onlineMeeting (object): onlineMeeting
            onlineMeetingProvider (string): onlineMeetingProvider
            onlineMeetingUrl (string): A URL for an online meeting. The property is set only when an organizer specifies in Outlook that an event is an online meeting such as Skype. Read-only.To access the URL to join an online meeting, use joinUrl which is exposed via the onlineMeeting property of the event. The onlineMeetingUrl property will be deprecated in the future.
            organizer (object): organizer
            originalEndTimeZone (string): The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            originalStart (string): Represents the start time of an event when it's initially created as an occurrence or exception in a recurring series. This property is not returned for events that are single instances. Its date and time information is expressed in ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            originalStartTimeZone (string): The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            recurrence (object): recurrence
            reminderMinutesBeforeStart (number): The number of minutes before the event start time that the reminder alert occurs.
            responseRequested (boolean): Default is true, which represents the organizer would like an invitee to send a response to the event.
            responseStatus (object): responseStatus
            sensitivity (string): sensitivity
            seriesMasterId (string): The ID for the recurring series master item, if this event is part of a recurring series.
            showAs (string): showAs
            start (object): start
            subject (string): The text of the event's subject line.
            transactionId (string): A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. It's useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you can't change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.
            type (string): type
            webLink (string): The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can't be accessed from within an iFrame.
            attachments (array): The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
            calendar (string): calendar
            extensions (array): The collection of open extensions defined for the event. Nullable.
            instances (array): The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions modified, but doesn't include occurrences cancelled from the series. Navigation property. Read-only. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the event. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the event. Read-only. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "allowNewTimeProposals": allowNewTimeProposals,
            "attendees": attendees,
            "body": body,
            "bodyPreview": bodyPreview,
            "end": end,
            "hasAttachments": hasAttachments,
            "hideAttendees": hideAttendees,
            "iCalUId": iCalUId,
            "importance": importance,
            "isAllDay": isAllDay,
            "isCancelled": isCancelled,
            "isDraft": isDraft,
            "isOnlineMeeting": isOnlineMeeting,
            "isOrganizer": isOrganizer,
            "isReminderOn": isReminderOn,
            "location": location,
            "locations": locations,
            "onlineMeeting": onlineMeeting,
            "onlineMeetingProvider": onlineMeetingProvider,
            "onlineMeetingUrl": onlineMeetingUrl,
            "organizer": organizer,
            "originalEndTimeZone": originalEndTimeZone,
            "originalStart": originalStart,
            "originalStartTimeZone": originalStartTimeZone,
            "recurrence": recurrence,
            "reminderMinutesBeforeStart": reminderMinutesBeforeStart,
            "responseRequested": responseRequested,
            "responseStatus": responseStatus,
            "sensitivity": sensitivity,
            "seriesMasterId": seriesMasterId,
            "showAs": showAs,
            "start": start,
            "subject": subject,
            "transactionId": transactionId,
            "type": type,
            "webLink": webLink,
            "attachments": attachments,
            "calendar": calendar,
            "extensions": extensions,
            "instances": instances,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_get_event(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get events from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_update_event(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        allowNewTimeProposals: Optional[bool] = None,
        attendees: Optional[List[Any]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        end: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        hideAttendees: Optional[bool] = None,
        iCalUId: Optional[str] = None,
        importance: Optional[str] = None,
        isAllDay: Optional[bool] = None,
        isCancelled: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isOnlineMeeting: Optional[bool] = None,
        isOrganizer: Optional[bool] = None,
        isReminderOn: Optional[bool] = None,
        location: Optional[dict[str, dict[str, Any]]] = None,
        locations: Optional[List[dict[str, dict[str, Any]]]] = None,
        onlineMeeting: Optional[dict[str, dict[str, Any]]] = None,
        onlineMeetingProvider: Optional[str] = None,
        onlineMeetingUrl: Optional[str] = None,
        organizer: Optional[dict[str, dict[str, Any]]] = None,
        originalEndTimeZone: Optional[str] = None,
        originalStart: Optional[str] = None,
        originalStartTimeZone: Optional[str] = None,
        recurrence: Optional[dict[str, dict[str, Any]]] = None,
        reminderMinutesBeforeStart: Optional[float] = None,
        responseRequested: Optional[bool] = None,
        responseStatus: Optional[dict[str, dict[str, Any]]] = None,
        sensitivity: Optional[str] = None,
        seriesMasterId: Optional[str] = None,
        showAs: Optional[str] = None,
        start: Optional[dict[str, dict[str, Any]]] = None,
        subject: Optional[str] = None,
        transactionId: Optional[str] = None,
        type: Optional[str] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        calendar: Optional[Any] = None,
        extensions: Optional[List[Any]] = None,
        instances: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property events in users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            allowNewTimeProposals (boolean): true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. The default is true.
            attendees (array): The collection of attendees for the event.
            body (object): body
            bodyPreview (string): The preview of the message associated with the event. It's in text format.
            end (object): end
            hasAttachments (boolean): Set to true if the event has attachments.
            hideAttendees (boolean): When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. The default is false.
            iCalUId (string): A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
            importance (string): importance
            isAllDay (boolean): Set to true if the event lasts all day. If true, regardless of whether it's a single-day or multi-day event, start, and endtime must be set to midnight and be in the same time zone.
            isCancelled (boolean): Set to true if the event has been canceled.
            isDraft (boolean): Set to true if the user has updated the meeting in Outlook but hasn't sent the updates to attendees. Set to false if all changes are sent, or if the event is an appointment without any attendees.
            isOnlineMeeting (boolean): True if this event has online meeting information (that is, onlineMeeting points to an onlineMeetingInfo resource), false otherwise. Default is false (onlineMeeting is null). Optional.  After you set isOnlineMeeting to true, Microsoft Graph initializes onlineMeeting. Subsequently, Outlook ignores any further changes to isOnlineMeeting, and the meeting remains available online.
            isOrganizer (boolean): Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). It also applies if a delegate organized the event on behalf of the owner.
            isReminderOn (boolean): Set to true if an alert is set to remind the user of the event.
            location (object): location
            locations (array): The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection are removed and replaced by the new location value.
            onlineMeeting (object): onlineMeeting
            onlineMeetingProvider (string): onlineMeetingProvider
            onlineMeetingUrl (string): A URL for an online meeting. The property is set only when an organizer specifies in Outlook that an event is an online meeting such as Skype. Read-only.To access the URL to join an online meeting, use joinUrl which is exposed via the onlineMeeting property of the event. The onlineMeetingUrl property will be deprecated in the future.
            organizer (object): organizer
            originalEndTimeZone (string): The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            originalStart (string): Represents the start time of an event when it's initially created as an occurrence or exception in a recurring series. This property is not returned for events that are single instances. Its date and time information is expressed in ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            originalStartTimeZone (string): The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            recurrence (object): recurrence
            reminderMinutesBeforeStart (number): The number of minutes before the event start time that the reminder alert occurs.
            responseRequested (boolean): Default is true, which represents the organizer would like an invitee to send a response to the event.
            responseStatus (object): responseStatus
            sensitivity (string): sensitivity
            seriesMasterId (string): The ID for the recurring series master item, if this event is part of a recurring series.
            showAs (string): showAs
            start (object): start
            subject (string): The text of the event's subject line.
            transactionId (string): A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. It's useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you can't change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.
            type (string): type
            webLink (string): The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can't be accessed from within an iFrame.
            attachments (array): The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
            calendar (string): calendar
            extensions (array): The collection of open extensions defined for the event. Nullable.
            instances (array): The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions modified, but doesn't include occurrences cancelled from the series. Navigation property. Read-only. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the event. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the event. Read-only. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "allowNewTimeProposals": allowNewTimeProposals,
            "attendees": attendees,
            "body": body,
            "bodyPreview": bodyPreview,
            "end": end,
            "hasAttachments": hasAttachments,
            "hideAttendees": hideAttendees,
            "iCalUId": iCalUId,
            "importance": importance,
            "isAllDay": isAllDay,
            "isCancelled": isCancelled,
            "isDraft": isDraft,
            "isOnlineMeeting": isOnlineMeeting,
            "isOrganizer": isOrganizer,
            "isReminderOn": isReminderOn,
            "location": location,
            "locations": locations,
            "onlineMeeting": onlineMeeting,
            "onlineMeetingProvider": onlineMeetingProvider,
            "onlineMeetingUrl": onlineMeetingUrl,
            "organizer": organizer,
            "originalEndTimeZone": originalEndTimeZone,
            "originalStart": originalStart,
            "originalStartTimeZone": originalStartTimeZone,
            "recurrence": recurrence,
            "reminderMinutesBeforeStart": reminderMinutesBeforeStart,
            "responseRequested": responseRequested,
            "responseStatus": responseStatus,
            "sensitivity": sensitivity,
            "seriesMasterId": seriesMasterId,
            "showAs": showAs,
            "start": start,
            "subject": subject,
            "transactionId": transactionId,
            "type": type,
            "webLink": webLink,
            "attachments": attachments,
            "calendar": calendar,
            "extensions": extensions,
            "instances": instances,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_delete_event(
        self, user_id: str, calendarGroup_id: str, calendar_id: str, event_id: str
    ) -> Any:
        """

        Delete navigation property events for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_list_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_create_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_get_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_delete_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        attachment_id: str,
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_attachment_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_attachment_create_upload_session(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_get_calendar(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_list_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_create_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_get_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_update_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_delete_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        extension_id: str,
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_extension_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_list_instance(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_get_instance(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_list_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_create_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_get_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_delete_attachment(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_attachment_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_attachment_create_upload_session(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_get_calendar(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_list_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_create_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_get_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_update_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_delete_extension(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_extension_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_accept(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_cancel(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_decline(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_dismiss_reminder(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_forward(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_permanent_delete(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_snooze_reminder(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_tentatively_accept(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_instance_delta(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/instances/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_accept(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_cancel(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_decline(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_dismiss_reminder(
        self, user_id: str, calendarGroup_id: str, calendar_id: str, event_id: str
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_forward(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_permanent_delete(
        self, user_id: str, calendarGroup_id: str, calendar_id: str, event_id: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_snooze_reminder(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_tentatively_accept(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_event_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_event_delta(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/events/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_allowed_calendar_sharing_role(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        User: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
    ) -> dict[str, Any]:
        """

        Invoke function allowedCalendarSharingRoles

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            User (string): User
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if User is None:
            raise ValueError("Missing required parameter 'User'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/microsoft.graph.allowedCalendarSharingRoles(User='{User}')"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_calendar_get_schedule(
        self,
        user_id: str,
        calendarGroup_id: str,
        calendar_id: str,
        Schedules: Optional[List[str]] = None,
        EndTime: Optional[dict[str, dict[str, Any]]] = None,
        StartTime: Optional[dict[str, dict[str, Any]]] = None,
        AvailabilityViewInterval: Optional[float] = None,
    ) -> dict[str, Any]:
        """

        Invoke action getSchedule

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id
            Schedules (array): Schedules
            EndTime (object): EndTime
            StartTime (object): StartTime
            AvailabilityViewInterval (number): AvailabilityViewInterval

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        request_body_data = None
        request_body_data = {
            "Schedules": Schedules,
            "EndTime": EndTime,
            "StartTime": StartTime,
            "AvailabilityViewInterval": AvailabilityViewInterval,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/microsoft.graph.getSchedule"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_permanent_delete(
        self, user_id: str, calendarGroup_id: str, calendar_id: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            calendar_id (string): calendar-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/{calendar_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_group_calendar_get_count(
        self,
        user_id: str,
        calendarGroup_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendarGroup_id (string): calendarGroup-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendarGroup_id is None:
            raise ValueError("Missing required parameter 'calendarGroup-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/{calendarGroup_id}/calendars/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_group_get_count(
        self, user_id: str, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendarGroup
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarGroups/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_list_calendar(
        self,
        user_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get calendars from users

        Args:
            user_id (string): user-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_create_calendar(
        self,
        user_id: str,
        id: Optional[str] = None,
        allowedOnlineMeetingProviders: Optional[List[str]] = None,
        canEdit: Optional[bool] = None,
        canShare: Optional[bool] = None,
        canViewPrivateItems: Optional[bool] = None,
        changeKey: Optional[str] = None,
        color: Optional[str] = None,
        defaultOnlineMeetingProvider: Optional[str] = None,
        hexColor: Optional[str] = None,
        isDefaultCalendar: Optional[bool] = None,
        isRemovable: Optional[bool] = None,
        isTallyingResponses: Optional[bool] = None,
        name: Optional[str] = None,
        owner: Optional[dict[str, dict[str, Any]]] = None,
        calendarPermissions: Optional[List[Any]] = None,
        calendarView: Optional[List[Any]] = None,
        events: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to calendars for users

        Args:
            user_id (string): user-id
            id (string): The unique identifier for an entity. Read-only.
            allowedOnlineMeetingProviders (array): Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
            canEdit (boolean): true if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who shared a calendar and granted write access.
            canShare (boolean): true if the user has permission to share the calendar, false otherwise. Only the user who created the calendar can share it.
            canViewPrivateItems (boolean): If true, the user can read calendar items that have been marked private, false otherwise.
            changeKey (string): Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            color (string): color
            defaultOnlineMeetingProvider (string): defaultOnlineMeetingProvider
            hexColor (string): The calendar color, expressed in a hex color code of three hexadecimal values, each ranging from 00 to FF and representing the red, green, or blue components of the color in the RGB color space. If the user has never explicitly set a color for the calendar, this property is empty. Read-only.
            isDefaultCalendar (boolean): true if this is the default calendar where new events are created by default, false otherwise.
            isRemovable (boolean): Indicates whether this user calendar can be deleted from the user mailbox.
            isTallyingResponses (boolean): Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.
            name (string): The calendar name.
            owner (object): owner
            calendarPermissions (array): The permissions of the users with whom the calendar is shared.
            calendarView (array): The calendar view for the calendar. Navigation property. Read-only.
            events (array): The events in the calendar. Navigation property. Read-only.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the calendar. Read-only. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "allowedOnlineMeetingProviders": allowedOnlineMeetingProviders,
            "canEdit": canEdit,
            "canShare": canShare,
            "canViewPrivateItems": canViewPrivateItems,
            "changeKey": changeKey,
            "color": color,
            "defaultOnlineMeetingProvider": defaultOnlineMeetingProvider,
            "hexColor": hexColor,
            "isDefaultCalendar": isDefaultCalendar,
            "isRemovable": isRemovable,
            "isTallyingResponses": isTallyingResponses,
            "name": name,
            "owner": owner,
            "calendarPermissions": calendarPermissions,
            "calendarView": calendarView,
            "events": events,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_get_calendar(
        self,
        user_id: str,
        calendar_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendars from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_update_calendar(
        self,
        user_id: str,
        calendar_id: str,
        id: Optional[str] = None,
        allowedOnlineMeetingProviders: Optional[List[str]] = None,
        canEdit: Optional[bool] = None,
        canShare: Optional[bool] = None,
        canViewPrivateItems: Optional[bool] = None,
        changeKey: Optional[str] = None,
        color: Optional[str] = None,
        defaultOnlineMeetingProvider: Optional[str] = None,
        hexColor: Optional[str] = None,
        isDefaultCalendar: Optional[bool] = None,
        isRemovable: Optional[bool] = None,
        isTallyingResponses: Optional[bool] = None,
        name: Optional[str] = None,
        owner: Optional[dict[str, dict[str, Any]]] = None,
        calendarPermissions: Optional[List[Any]] = None,
        calendarView: Optional[List[Any]] = None,
        events: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property calendars in users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            id (string): The unique identifier for an entity. Read-only.
            allowedOnlineMeetingProviders (array): Represent the online meeting service providers that can be used to create online meetings in this calendar. Possible values are: unknown, skypeForBusiness, skypeForConsumer, teamsForBusiness.
            canEdit (boolean): true if the user can write to the calendar, false otherwise. This property is true for the user who created the calendar. This property is also true for a user who shared a calendar and granted write access.
            canShare (boolean): true if the user has permission to share the calendar, false otherwise. Only the user who created the calendar can share it.
            canViewPrivateItems (boolean): If true, the user can read calendar items that have been marked private, false otherwise.
            changeKey (string): Identifies the version of the calendar object. Every time the calendar is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            color (string): color
            defaultOnlineMeetingProvider (string): defaultOnlineMeetingProvider
            hexColor (string): The calendar color, expressed in a hex color code of three hexadecimal values, each ranging from 00 to FF and representing the red, green, or blue components of the color in the RGB color space. If the user has never explicitly set a color for the calendar, this property is empty. Read-only.
            isDefaultCalendar (boolean): true if this is the default calendar where new events are created by default, false otherwise.
            isRemovable (boolean): Indicates whether this user calendar can be deleted from the user mailbox.
            isTallyingResponses (boolean): Indicates whether this user calendar supports tracking of meeting responses. Only meeting invites sent from users' primary calendars support tracking of meeting responses.
            name (string): The calendar name.
            owner (object): owner
            calendarPermissions (array): The permissions of the users with whom the calendar is shared.
            calendarView (array): The calendar view for the calendar. Navigation property. Read-only.
            events (array): The events in the calendar. Navigation property. Read-only.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the calendar. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the calendar. Read-only. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "allowedOnlineMeetingProviders": allowedOnlineMeetingProviders,
            "canEdit": canEdit,
            "canShare": canShare,
            "canViewPrivateItems": canViewPrivateItems,
            "changeKey": changeKey,
            "color": color,
            "defaultOnlineMeetingProvider": defaultOnlineMeetingProvider,
            "hexColor": hexColor,
            "isDefaultCalendar": isDefaultCalendar,
            "isRemovable": isRemovable,
            "isTallyingResponses": isTallyingResponses,
            "name": name,
            "owner": owner,
            "calendarPermissions": calendarPermissions,
            "calendarView": calendarView,
            "events": events,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_delete_calendar(self, user_id: str, calendar_id: str) -> Any:
        """

        Delete navigation property calendars for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_list_calendar_permission(
        self,
        user_id: str,
        calendar_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get calendarPermissions from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarPermissions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_create_calendar_permission(
        self,
        user_id: str,
        calendar_id: str,
        id: Optional[str] = None,
        allowedRoles: Optional[List[str]] = None,
        emailAddress: Optional[dict[str, dict[str, Any]]] = None,
        isInsideOrganization: Optional[bool] = None,
        isRemovable: Optional[bool] = None,
        role: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to calendarPermissions for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            id (string): The unique identifier for an entity. Read-only.
            allowedRoles (array): List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.
            emailAddress (object): emailAddress
            isInsideOrganization (boolean): True if the user in context (recipient or delegate) is inside the same organization as the calendar owner.
            isRemovable (boolean): True if the user can be removed from the list of recipients or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You can't remove 'My organization' as a share recipient to a calendar.
            role (string): role

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "allowedRoles": allowedRoles,
            "emailAddress": emailAddress,
            "isInsideOrganization": isInsideOrganization,
            "isRemovable": isRemovable,
            "role": role,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarPermissions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_get_calendar_permission(
        self,
        user_id: str,
        calendar_id: str,
        calendarPermission_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendarPermissions from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            calendarPermission_id (string): calendarPermission-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if calendarPermission_id is None:
            raise ValueError("Missing required parameter 'calendarPermission-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarPermissions/{calendarPermission_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_update_calendar_permission(
        self,
        user_id: str,
        calendar_id: str,
        calendarPermission_id: str,
        id: Optional[str] = None,
        allowedRoles: Optional[List[str]] = None,
        emailAddress: Optional[dict[str, dict[str, Any]]] = None,
        isInsideOrganization: Optional[bool] = None,
        isRemovable: Optional[bool] = None,
        role: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property calendarPermissions in users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            calendarPermission_id (string): calendarPermission-id
            id (string): The unique identifier for an entity. Read-only.
            allowedRoles (array): List of allowed sharing or delegating permission levels for the calendar. Possible values are: none, freeBusyRead, limitedRead, read, write, delegateWithoutPrivateEventAccess, delegateWithPrivateEventAccess, custom.
            emailAddress (object): emailAddress
            isInsideOrganization (boolean): True if the user in context (recipient or delegate) is inside the same organization as the calendar owner.
            isRemovable (boolean): True if the user can be removed from the list of recipients or delegates for the specified calendar, false otherwise. The 'My organization' user determines the permissions other people within your organization have to the given calendar. You can't remove 'My organization' as a share recipient to a calendar.
            role (string): role

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if calendarPermission_id is None:
            raise ValueError("Missing required parameter 'calendarPermission-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "allowedRoles": allowedRoles,
            "emailAddress": emailAddress,
            "isInsideOrganization": isInsideOrganization,
            "isRemovable": isRemovable,
            "role": role,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarPermissions/{calendarPermission_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_delete_calendar_permission(
        self, user_id: str, calendar_id: str, calendarPermission_id: str
    ) -> Any:
        """

        Delete navigation property calendarPermissions for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            calendarPermission_id (string): calendarPermission-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if calendarPermission_id is None:
            raise ValueError("Missing required parameter 'calendarPermission-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarPermissions/{calendarPermission_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_permission_get_count(
        self,
        user_id: str,
        calendar_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarPermissions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_list_calendar_view(
        self,
        user_id: str,
        calendar_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get calendarView from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_get_calendar_view(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendarView from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_list_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_create_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_get_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_delete_attachment(
        self, user_id: str, calendar_id: str, event_id: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_attachment_get_count(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_attachment_create_upload_session(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_get_calendar(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_list_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_create_extension(
        self, user_id: str, calendar_id: str, event_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_get_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_update_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_delete_extension(
        self, user_id: str, calendar_id: str, event_id: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_extension_get_count(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_list_instance(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_get_instance(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_list_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_create_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_get_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_delete_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_attachment_get_count(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_attachment_create_upload_session(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_get_calendar(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_list_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_create_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_get_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_update_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_delete_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_extension_get_count(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_accept(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_cancel(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_decline(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_dismiss_reminder(
        self, user_id: str, calendar_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_forward(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_permanent_delete(
        self, user_id: str, calendar_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_snooze_reminder(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_tentatively_accept(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_get_count(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_instance_delta(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/instances/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_accept(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_cancel(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_decline(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_dismiss_reminder(
        self, user_id: str, calendar_id: str, event_id: str
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_forward(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_permanent_delete(
        self, user_id: str, calendar_id: str, event_id: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_snooze_reminder(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_tentatively_accept(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/{event_id}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_calendar_view_get_count(
        self,
        user_id: str,
        calendar_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_calendar_view_delta(
        self,
        user_id: str,
        calendar_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/calendarView/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_list_event(
        self,
        user_id: str,
        calendar_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get events from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_create_event(
        self,
        user_id: str,
        calendar_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        allowNewTimeProposals: Optional[bool] = None,
        attendees: Optional[List[Any]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        end: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        hideAttendees: Optional[bool] = None,
        iCalUId: Optional[str] = None,
        importance: Optional[str] = None,
        isAllDay: Optional[bool] = None,
        isCancelled: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isOnlineMeeting: Optional[bool] = None,
        isOrganizer: Optional[bool] = None,
        isReminderOn: Optional[bool] = None,
        location: Optional[dict[str, dict[str, Any]]] = None,
        locations: Optional[List[dict[str, dict[str, Any]]]] = None,
        onlineMeeting: Optional[dict[str, dict[str, Any]]] = None,
        onlineMeetingProvider: Optional[str] = None,
        onlineMeetingUrl: Optional[str] = None,
        organizer: Optional[dict[str, dict[str, Any]]] = None,
        originalEndTimeZone: Optional[str] = None,
        originalStart: Optional[str] = None,
        originalStartTimeZone: Optional[str] = None,
        recurrence: Optional[dict[str, dict[str, Any]]] = None,
        reminderMinutesBeforeStart: Optional[float] = None,
        responseRequested: Optional[bool] = None,
        responseStatus: Optional[dict[str, dict[str, Any]]] = None,
        sensitivity: Optional[str] = None,
        seriesMasterId: Optional[str] = None,
        showAs: Optional[str] = None,
        start: Optional[dict[str, dict[str, Any]]] = None,
        subject: Optional[str] = None,
        transactionId: Optional[str] = None,
        type: Optional[str] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        calendar: Optional[Any] = None,
        extensions: Optional[List[Any]] = None,
        instances: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to events for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            allowNewTimeProposals (boolean): true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. The default is true.
            attendees (array): The collection of attendees for the event.
            body (object): body
            bodyPreview (string): The preview of the message associated with the event. It's in text format.
            end (object): end
            hasAttachments (boolean): Set to true if the event has attachments.
            hideAttendees (boolean): When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. The default is false.
            iCalUId (string): A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
            importance (string): importance
            isAllDay (boolean): Set to true if the event lasts all day. If true, regardless of whether it's a single-day or multi-day event, start, and endtime must be set to midnight and be in the same time zone.
            isCancelled (boolean): Set to true if the event has been canceled.
            isDraft (boolean): Set to true if the user has updated the meeting in Outlook but hasn't sent the updates to attendees. Set to false if all changes are sent, or if the event is an appointment without any attendees.
            isOnlineMeeting (boolean): True if this event has online meeting information (that is, onlineMeeting points to an onlineMeetingInfo resource), false otherwise. Default is false (onlineMeeting is null). Optional.  After you set isOnlineMeeting to true, Microsoft Graph initializes onlineMeeting. Subsequently, Outlook ignores any further changes to isOnlineMeeting, and the meeting remains available online.
            isOrganizer (boolean): Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). It also applies if a delegate organized the event on behalf of the owner.
            isReminderOn (boolean): Set to true if an alert is set to remind the user of the event.
            location (object): location
            locations (array): The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection are removed and replaced by the new location value.
            onlineMeeting (object): onlineMeeting
            onlineMeetingProvider (string): onlineMeetingProvider
            onlineMeetingUrl (string): A URL for an online meeting. The property is set only when an organizer specifies in Outlook that an event is an online meeting such as Skype. Read-only.To access the URL to join an online meeting, use joinUrl which is exposed via the onlineMeeting property of the event. The onlineMeetingUrl property will be deprecated in the future.
            organizer (object): organizer
            originalEndTimeZone (string): The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            originalStart (string): Represents the start time of an event when it's initially created as an occurrence or exception in a recurring series. This property is not returned for events that are single instances. Its date and time information is expressed in ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            originalStartTimeZone (string): The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            recurrence (object): recurrence
            reminderMinutesBeforeStart (number): The number of minutes before the event start time that the reminder alert occurs.
            responseRequested (boolean): Default is true, which represents the organizer would like an invitee to send a response to the event.
            responseStatus (object): responseStatus
            sensitivity (string): sensitivity
            seriesMasterId (string): The ID for the recurring series master item, if this event is part of a recurring series.
            showAs (string): showAs
            start (object): start
            subject (string): The text of the event's subject line.
            transactionId (string): A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. It's useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you can't change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.
            type (string): type
            webLink (string): The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can't be accessed from within an iFrame.
            attachments (array): The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
            calendar (string): calendar
            extensions (array): The collection of open extensions defined for the event. Nullable.
            instances (array): The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions modified, but doesn't include occurrences cancelled from the series. Navigation property. Read-only. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the event. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the event. Read-only. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "allowNewTimeProposals": allowNewTimeProposals,
            "attendees": attendees,
            "body": body,
            "bodyPreview": bodyPreview,
            "end": end,
            "hasAttachments": hasAttachments,
            "hideAttendees": hideAttendees,
            "iCalUId": iCalUId,
            "importance": importance,
            "isAllDay": isAllDay,
            "isCancelled": isCancelled,
            "isDraft": isDraft,
            "isOnlineMeeting": isOnlineMeeting,
            "isOrganizer": isOrganizer,
            "isReminderOn": isReminderOn,
            "location": location,
            "locations": locations,
            "onlineMeeting": onlineMeeting,
            "onlineMeetingProvider": onlineMeetingProvider,
            "onlineMeetingUrl": onlineMeetingUrl,
            "organizer": organizer,
            "originalEndTimeZone": originalEndTimeZone,
            "originalStart": originalStart,
            "originalStartTimeZone": originalStartTimeZone,
            "recurrence": recurrence,
            "reminderMinutesBeforeStart": reminderMinutesBeforeStart,
            "responseRequested": responseRequested,
            "responseStatus": responseStatus,
            "sensitivity": sensitivity,
            "seriesMasterId": seriesMasterId,
            "showAs": showAs,
            "start": start,
            "subject": subject,
            "transactionId": transactionId,
            "type": type,
            "webLink": webLink,
            "attachments": attachments,
            "calendar": calendar,
            "extensions": extensions,
            "instances": instances,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_get_event(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get events from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_update_event(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        allowNewTimeProposals: Optional[bool] = None,
        attendees: Optional[List[Any]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        end: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        hideAttendees: Optional[bool] = None,
        iCalUId: Optional[str] = None,
        importance: Optional[str] = None,
        isAllDay: Optional[bool] = None,
        isCancelled: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isOnlineMeeting: Optional[bool] = None,
        isOrganizer: Optional[bool] = None,
        isReminderOn: Optional[bool] = None,
        location: Optional[dict[str, dict[str, Any]]] = None,
        locations: Optional[List[dict[str, dict[str, Any]]]] = None,
        onlineMeeting: Optional[dict[str, dict[str, Any]]] = None,
        onlineMeetingProvider: Optional[str] = None,
        onlineMeetingUrl: Optional[str] = None,
        organizer: Optional[dict[str, dict[str, Any]]] = None,
        originalEndTimeZone: Optional[str] = None,
        originalStart: Optional[str] = None,
        originalStartTimeZone: Optional[str] = None,
        recurrence: Optional[dict[str, dict[str, Any]]] = None,
        reminderMinutesBeforeStart: Optional[float] = None,
        responseRequested: Optional[bool] = None,
        responseStatus: Optional[dict[str, dict[str, Any]]] = None,
        sensitivity: Optional[str] = None,
        seriesMasterId: Optional[str] = None,
        showAs: Optional[str] = None,
        start: Optional[dict[str, dict[str, Any]]] = None,
        subject: Optional[str] = None,
        transactionId: Optional[str] = None,
        type: Optional[str] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        calendar: Optional[Any] = None,
        extensions: Optional[List[Any]] = None,
        instances: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property events in users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            allowNewTimeProposals (boolean): true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. The default is true.
            attendees (array): The collection of attendees for the event.
            body (object): body
            bodyPreview (string): The preview of the message associated with the event. It's in text format.
            end (object): end
            hasAttachments (boolean): Set to true if the event has attachments.
            hideAttendees (boolean): When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. The default is false.
            iCalUId (string): A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
            importance (string): importance
            isAllDay (boolean): Set to true if the event lasts all day. If true, regardless of whether it's a single-day or multi-day event, start, and endtime must be set to midnight and be in the same time zone.
            isCancelled (boolean): Set to true if the event has been canceled.
            isDraft (boolean): Set to true if the user has updated the meeting in Outlook but hasn't sent the updates to attendees. Set to false if all changes are sent, or if the event is an appointment without any attendees.
            isOnlineMeeting (boolean): True if this event has online meeting information (that is, onlineMeeting points to an onlineMeetingInfo resource), false otherwise. Default is false (onlineMeeting is null). Optional.  After you set isOnlineMeeting to true, Microsoft Graph initializes onlineMeeting. Subsequently, Outlook ignores any further changes to isOnlineMeeting, and the meeting remains available online.
            isOrganizer (boolean): Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). It also applies if a delegate organized the event on behalf of the owner.
            isReminderOn (boolean): Set to true if an alert is set to remind the user of the event.
            location (object): location
            locations (array): The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection are removed and replaced by the new location value.
            onlineMeeting (object): onlineMeeting
            onlineMeetingProvider (string): onlineMeetingProvider
            onlineMeetingUrl (string): A URL for an online meeting. The property is set only when an organizer specifies in Outlook that an event is an online meeting such as Skype. Read-only.To access the URL to join an online meeting, use joinUrl which is exposed via the onlineMeeting property of the event. The onlineMeetingUrl property will be deprecated in the future.
            organizer (object): organizer
            originalEndTimeZone (string): The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            originalStart (string): Represents the start time of an event when it's initially created as an occurrence or exception in a recurring series. This property is not returned for events that are single instances. Its date and time information is expressed in ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            originalStartTimeZone (string): The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            recurrence (object): recurrence
            reminderMinutesBeforeStart (number): The number of minutes before the event start time that the reminder alert occurs.
            responseRequested (boolean): Default is true, which represents the organizer would like an invitee to send a response to the event.
            responseStatus (object): responseStatus
            sensitivity (string): sensitivity
            seriesMasterId (string): The ID for the recurring series master item, if this event is part of a recurring series.
            showAs (string): showAs
            start (object): start
            subject (string): The text of the event's subject line.
            transactionId (string): A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. It's useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you can't change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.
            type (string): type
            webLink (string): The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can't be accessed from within an iFrame.
            attachments (array): The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
            calendar (string): calendar
            extensions (array): The collection of open extensions defined for the event. Nullable.
            instances (array): The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions modified, but doesn't include occurrences cancelled from the series. Navigation property. Read-only. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the event. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the event. Read-only. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "allowNewTimeProposals": allowNewTimeProposals,
            "attendees": attendees,
            "body": body,
            "bodyPreview": bodyPreview,
            "end": end,
            "hasAttachments": hasAttachments,
            "hideAttendees": hideAttendees,
            "iCalUId": iCalUId,
            "importance": importance,
            "isAllDay": isAllDay,
            "isCancelled": isCancelled,
            "isDraft": isDraft,
            "isOnlineMeeting": isOnlineMeeting,
            "isOrganizer": isOrganizer,
            "isReminderOn": isReminderOn,
            "location": location,
            "locations": locations,
            "onlineMeeting": onlineMeeting,
            "onlineMeetingProvider": onlineMeetingProvider,
            "onlineMeetingUrl": onlineMeetingUrl,
            "organizer": organizer,
            "originalEndTimeZone": originalEndTimeZone,
            "originalStart": originalStart,
            "originalStartTimeZone": originalStartTimeZone,
            "recurrence": recurrence,
            "reminderMinutesBeforeStart": reminderMinutesBeforeStart,
            "responseRequested": responseRequested,
            "responseStatus": responseStatus,
            "sensitivity": sensitivity,
            "seriesMasterId": seriesMasterId,
            "showAs": showAs,
            "start": start,
            "subject": subject,
            "transactionId": transactionId,
            "type": type,
            "webLink": webLink,
            "attachments": attachments,
            "calendar": calendar,
            "extensions": extensions,
            "instances": instances,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_delete_event(
        self, user_id: str, calendar_id: str, event_id: str
    ) -> Any:
        """

        Delete navigation property events for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_list_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_create_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_get_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_delete_attachment(
        self, user_id: str, calendar_id: str, event_id: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_attachment_get_count(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_attachment_create_upload_session(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_get_calendar(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_list_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_create_extension(
        self, user_id: str, calendar_id: str, event_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_get_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_update_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_delete_extension(
        self, user_id: str, calendar_id: str, event_id: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_extension_get_count(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_list_instance(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_get_instance(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_list_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_create_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_get_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_delete_attachment(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_attachment_get_count(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_attachment_create_upload_session(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_get_calendar(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_list_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_create_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_get_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_update_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_delete_extension(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_extension_get_count(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_accept(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_cancel(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_decline(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_dismiss_reminder(
        self, user_id: str, calendar_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_forward(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_permanent_delete(
        self, user_id: str, calendar_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_snooze_reminder(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_tentatively_accept(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_instance_get_count(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_instance_delta(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/instances/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_accept(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_cancel(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_decline(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_dismiss_reminder(
        self, user_id: str, calendar_id: str, event_id: str
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_forward(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_permanent_delete(
        self, user_id: str, calendar_id: str, event_id: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_snooze_reminder(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_tentatively_accept(
        self,
        user_id: str,
        calendar_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/{event_id}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_event_get_count(
        self,
        user_id: str,
        calendar_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_event_delta(
        self,
        user_id: str,
        calendar_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/events/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_allowed_calendar_sharing_role(
        self,
        user_id: str,
        calendar_id: str,
        User: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
    ) -> dict[str, Any]:
        """

        Invoke function allowedCalendarSharingRoles

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            User (string): User
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        if User is None:
            raise ValueError("Missing required parameter 'User'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/microsoft.graph.allowedCalendarSharingRoles(User='{User}')"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_get_schedule(
        self,
        user_id: str,
        calendar_id: str,
        Schedules: Optional[List[str]] = None,
        EndTime: Optional[dict[str, dict[str, Any]]] = None,
        StartTime: Optional[dict[str, dict[str, Any]]] = None,
        AvailabilityViewInterval: Optional[float] = None,
    ) -> dict[str, Any]:
        """

        Invoke action getSchedule

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id
            Schedules (array): Schedules
            EndTime (object): EndTime
            StartTime (object): StartTime
            AvailabilityViewInterval (number): AvailabilityViewInterval

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        request_body_data = None
        request_body_data = {
            "Schedules": Schedules,
            "EndTime": EndTime,
            "StartTime": StartTime,
            "AvailabilityViewInterval": AvailabilityViewInterval,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/microsoft.graph.getSchedule"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_permanent_delete(self, user_id: str, calendar_id: str) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            calendar_id (string): calendar-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if calendar_id is None:
            raise ValueError("Missing required parameter 'calendar-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/{calendar_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_get_count(
        self, user_id: str, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.calendar
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendars/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_list_calendar_view(
        self,
        user_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get calendarView from users

        Args:
            user_id (string): user-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_get_calendar_view(
        self,
        user_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendarView from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_list_attachment(
        self,
        user_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_create_attachment(
        self,
        user_id: str,
        event_id: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_get_attachment(
        self,
        user_id: str,
        event_id: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_delete_attachment(
        self, user_id: str, event_id: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_attachment_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_attachment_create_upload_session(
        self,
        user_id: str,
        event_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            event_id (string): event-id
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_get_calendar(
        self,
        user_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_list_extension(
        self,
        user_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_create_extension(
        self, user_id: str, event_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_get_extension(
        self,
        user_id: str,
        event_id: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_update_extension(
        self, user_id: str, event_id: str, extension_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_delete_extension(
        self, user_id: str, event_id: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_extension_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_list_instance(
        self,
        user_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_get_instance(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_list_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_create_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_instance_get_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_delete_attachment(
        self, user_id: str, event_id: str, event_id1: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_attachment_get_count(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_attachment_create_upload_session(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_instance_get_calendar(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_list_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_create_extension(
        self, user_id: str, event_id: str, event_id1: str, id: Optional[str] = None
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_instance_get_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_update_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_delete_extension(
        self, user_id: str, event_id: str, event_id1: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_extension_get_count(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_accept(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_instance_cancel(
        self, user_id: str, event_id: str, event_id1: str, Comment: Optional[str] = None
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_instance_decline(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_instance_dismiss_reminder(
        self, user_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_instance_forward(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_instance_permanent_delete(
        self, user_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_instance_snooze_reminder(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_instance_tentatively_accept(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/{event_id1}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_instance_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_instance_delta(
        self,
        user_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/instances/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_accept(
        self,
        user_id: str,
        event_id: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_cancel(
        self, user_id: str, event_id: str, Comment: Optional[str] = None
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            event_id (string): event-id
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_decline(
        self,
        user_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_dismiss_reminder(self, user_id: str, event_id: str) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_forward(
        self,
        user_id: str,
        event_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_permanent_delete(self, user_id: str, event_id: str) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_snooze_reminder(
        self,
        user_id: str,
        event_id: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_tentatively_accept(
        self,
        user_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/{event_id}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_calendar_view_get_count(
        self, user_id: str, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_calendar_view_delta(
        self,
        user_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/calendarView/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_list_event(
        self,
        user_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get events from users

        Args:
            user_id (string): user-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_create_event(
        self,
        user_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        allowNewTimeProposals: Optional[bool] = None,
        attendees: Optional[List[Any]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        end: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        hideAttendees: Optional[bool] = None,
        iCalUId: Optional[str] = None,
        importance: Optional[str] = None,
        isAllDay: Optional[bool] = None,
        isCancelled: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isOnlineMeeting: Optional[bool] = None,
        isOrganizer: Optional[bool] = None,
        isReminderOn: Optional[bool] = None,
        location: Optional[dict[str, dict[str, Any]]] = None,
        locations: Optional[List[dict[str, dict[str, Any]]]] = None,
        onlineMeeting: Optional[dict[str, dict[str, Any]]] = None,
        onlineMeetingProvider: Optional[str] = None,
        onlineMeetingUrl: Optional[str] = None,
        organizer: Optional[dict[str, dict[str, Any]]] = None,
        originalEndTimeZone: Optional[str] = None,
        originalStart: Optional[str] = None,
        originalStartTimeZone: Optional[str] = None,
        recurrence: Optional[dict[str, dict[str, Any]]] = None,
        reminderMinutesBeforeStart: Optional[float] = None,
        responseRequested: Optional[bool] = None,
        responseStatus: Optional[dict[str, dict[str, Any]]] = None,
        sensitivity: Optional[str] = None,
        seriesMasterId: Optional[str] = None,
        showAs: Optional[str] = None,
        start: Optional[dict[str, dict[str, Any]]] = None,
        subject: Optional[str] = None,
        transactionId: Optional[str] = None,
        type: Optional[str] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        calendar: Optional[Any] = None,
        extensions: Optional[List[Any]] = None,
        instances: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to events for users

        Args:
            user_id (string): user-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            allowNewTimeProposals (boolean): true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. The default is true.
            attendees (array): The collection of attendees for the event.
            body (object): body
            bodyPreview (string): The preview of the message associated with the event. It's in text format.
            end (object): end
            hasAttachments (boolean): Set to true if the event has attachments.
            hideAttendees (boolean): When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. The default is false.
            iCalUId (string): A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
            importance (string): importance
            isAllDay (boolean): Set to true if the event lasts all day. If true, regardless of whether it's a single-day or multi-day event, start, and endtime must be set to midnight and be in the same time zone.
            isCancelled (boolean): Set to true if the event has been canceled.
            isDraft (boolean): Set to true if the user has updated the meeting in Outlook but hasn't sent the updates to attendees. Set to false if all changes are sent, or if the event is an appointment without any attendees.
            isOnlineMeeting (boolean): True if this event has online meeting information (that is, onlineMeeting points to an onlineMeetingInfo resource), false otherwise. Default is false (onlineMeeting is null). Optional.  After you set isOnlineMeeting to true, Microsoft Graph initializes onlineMeeting. Subsequently, Outlook ignores any further changes to isOnlineMeeting, and the meeting remains available online.
            isOrganizer (boolean): Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). It also applies if a delegate organized the event on behalf of the owner.
            isReminderOn (boolean): Set to true if an alert is set to remind the user of the event.
            location (object): location
            locations (array): The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection are removed and replaced by the new location value.
            onlineMeeting (object): onlineMeeting
            onlineMeetingProvider (string): onlineMeetingProvider
            onlineMeetingUrl (string): A URL for an online meeting. The property is set only when an organizer specifies in Outlook that an event is an online meeting such as Skype. Read-only.To access the URL to join an online meeting, use joinUrl which is exposed via the onlineMeeting property of the event. The onlineMeetingUrl property will be deprecated in the future.
            organizer (object): organizer
            originalEndTimeZone (string): The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            originalStart (string): Represents the start time of an event when it's initially created as an occurrence or exception in a recurring series. This property is not returned for events that are single instances. Its date and time information is expressed in ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            originalStartTimeZone (string): The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            recurrence (object): recurrence
            reminderMinutesBeforeStart (number): The number of minutes before the event start time that the reminder alert occurs.
            responseRequested (boolean): Default is true, which represents the organizer would like an invitee to send a response to the event.
            responseStatus (object): responseStatus
            sensitivity (string): sensitivity
            seriesMasterId (string): The ID for the recurring series master item, if this event is part of a recurring series.
            showAs (string): showAs
            start (object): start
            subject (string): The text of the event's subject line.
            transactionId (string): A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. It's useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you can't change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.
            type (string): type
            webLink (string): The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can't be accessed from within an iFrame.
            attachments (array): The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
            calendar (string): calendar
            extensions (array): The collection of open extensions defined for the event. Nullable.
            instances (array): The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions modified, but doesn't include occurrences cancelled from the series. Navigation property. Read-only. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the event. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the event. Read-only. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "allowNewTimeProposals": allowNewTimeProposals,
            "attendees": attendees,
            "body": body,
            "bodyPreview": bodyPreview,
            "end": end,
            "hasAttachments": hasAttachments,
            "hideAttendees": hideAttendees,
            "iCalUId": iCalUId,
            "importance": importance,
            "isAllDay": isAllDay,
            "isCancelled": isCancelled,
            "isDraft": isDraft,
            "isOnlineMeeting": isOnlineMeeting,
            "isOrganizer": isOrganizer,
            "isReminderOn": isReminderOn,
            "location": location,
            "locations": locations,
            "onlineMeeting": onlineMeeting,
            "onlineMeetingProvider": onlineMeetingProvider,
            "onlineMeetingUrl": onlineMeetingUrl,
            "organizer": organizer,
            "originalEndTimeZone": originalEndTimeZone,
            "originalStart": originalStart,
            "originalStartTimeZone": originalStartTimeZone,
            "recurrence": recurrence,
            "reminderMinutesBeforeStart": reminderMinutesBeforeStart,
            "responseRequested": responseRequested,
            "responseStatus": responseStatus,
            "sensitivity": sensitivity,
            "seriesMasterId": seriesMasterId,
            "showAs": showAs,
            "start": start,
            "subject": subject,
            "transactionId": transactionId,
            "type": type,
            "webLink": webLink,
            "attachments": attachments,
            "calendar": calendar,
            "extensions": extensions,
            "instances": instances,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_get_event(
        self,
        user_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get events from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_update_event(
        self,
        user_id: str,
        event_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        allowNewTimeProposals: Optional[bool] = None,
        attendees: Optional[List[Any]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        end: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        hideAttendees: Optional[bool] = None,
        iCalUId: Optional[str] = None,
        importance: Optional[str] = None,
        isAllDay: Optional[bool] = None,
        isCancelled: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isOnlineMeeting: Optional[bool] = None,
        isOrganizer: Optional[bool] = None,
        isReminderOn: Optional[bool] = None,
        location: Optional[dict[str, dict[str, Any]]] = None,
        locations: Optional[List[dict[str, dict[str, Any]]]] = None,
        onlineMeeting: Optional[dict[str, dict[str, Any]]] = None,
        onlineMeetingProvider: Optional[str] = None,
        onlineMeetingUrl: Optional[str] = None,
        organizer: Optional[dict[str, dict[str, Any]]] = None,
        originalEndTimeZone: Optional[str] = None,
        originalStart: Optional[str] = None,
        originalStartTimeZone: Optional[str] = None,
        recurrence: Optional[dict[str, dict[str, Any]]] = None,
        reminderMinutesBeforeStart: Optional[float] = None,
        responseRequested: Optional[bool] = None,
        responseStatus: Optional[dict[str, dict[str, Any]]] = None,
        sensitivity: Optional[str] = None,
        seriesMasterId: Optional[str] = None,
        showAs: Optional[str] = None,
        start: Optional[dict[str, dict[str, Any]]] = None,
        subject: Optional[str] = None,
        transactionId: Optional[str] = None,
        type: Optional[str] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        calendar: Optional[Any] = None,
        extensions: Optional[List[Any]] = None,
        instances: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property events in users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            allowNewTimeProposals (boolean): true if the meeting organizer allows invitees to propose a new time when responding; otherwise, false. Optional. The default is true.
            attendees (array): The collection of attendees for the event.
            body (object): body
            bodyPreview (string): The preview of the message associated with the event. It's in text format.
            end (object): end
            hasAttachments (boolean): Set to true if the event has attachments.
            hideAttendees (boolean): When set to true, each attendee only sees themselves in the meeting request and meeting Tracking list. The default is false.
            iCalUId (string): A unique identifier for an event across calendars. This ID is different for each occurrence in a recurring series. Read-only.
            importance (string): importance
            isAllDay (boolean): Set to true if the event lasts all day. If true, regardless of whether it's a single-day or multi-day event, start, and endtime must be set to midnight and be in the same time zone.
            isCancelled (boolean): Set to true if the event has been canceled.
            isDraft (boolean): Set to true if the user has updated the meeting in Outlook but hasn't sent the updates to attendees. Set to false if all changes are sent, or if the event is an appointment without any attendees.
            isOnlineMeeting (boolean): True if this event has online meeting information (that is, onlineMeeting points to an onlineMeetingInfo resource), false otherwise. Default is false (onlineMeeting is null). Optional.  After you set isOnlineMeeting to true, Microsoft Graph initializes onlineMeeting. Subsequently, Outlook ignores any further changes to isOnlineMeeting, and the meeting remains available online.
            isOrganizer (boolean): Set to true if the calendar owner (specified by the owner property of the calendar) is the organizer of the event (specified by the organizer property of the event). It also applies if a delegate organized the event on behalf of the owner.
            isReminderOn (boolean): Set to true if an alert is set to remind the user of the event.
            location (object): location
            locations (array): The locations where the event is held or attended from. The location and locations properties always correspond with each other. If you update the location property, any prior locations in the locations collection are removed and replaced by the new location value.
            onlineMeeting (object): onlineMeeting
            onlineMeetingProvider (string): onlineMeetingProvider
            onlineMeetingUrl (string): A URL for an online meeting. The property is set only when an organizer specifies in Outlook that an event is an online meeting such as Skype. Read-only.To access the URL to join an online meeting, use joinUrl which is exposed via the onlineMeeting property of the event. The onlineMeetingUrl property will be deprecated in the future.
            organizer (object): organizer
            originalEndTimeZone (string): The end time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            originalStart (string): Represents the start time of an event when it's initially created as an occurrence or exception in a recurring series. This property is not returned for events that are single instances. Its date and time information is expressed in ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            originalStartTimeZone (string): The start time zone that was set when the event was created. A value of tzone://Microsoft/Custom indicates that a legacy custom time zone was set in desktop Outlook.
            recurrence (object): recurrence
            reminderMinutesBeforeStart (number): The number of minutes before the event start time that the reminder alert occurs.
            responseRequested (boolean): Default is true, which represents the organizer would like an invitee to send a response to the event.
            responseStatus (object): responseStatus
            sensitivity (string): sensitivity
            seriesMasterId (string): The ID for the recurring series master item, if this event is part of a recurring series.
            showAs (string): showAs
            start (object): start
            subject (string): The text of the event's subject line.
            transactionId (string): A custom identifier specified by a client app for the server to avoid redundant POST operations in case of client retries to create the same event. It's useful when low network connectivity causes the client to time out before receiving a response from the server for the client's prior create-event request. After you set transactionId when creating an event, you can't change transactionId in a subsequent update. This property is only returned in a response payload if an app has set it. Optional.
            type (string): type
            webLink (string): The URL to open the event in Outlook on the web.Outlook on the web opens the event in the browser if you are signed in to your mailbox. Otherwise, Outlook on the web prompts you to sign in.This URL can't be accessed from within an iFrame.
            attachments (array): The collection of FileAttachment, ItemAttachment, and referenceAttachment attachments for the event. Navigation property. Read-only. Nullable.
            calendar (string): calendar
            extensions (array): The collection of open extensions defined for the event. Nullable.
            instances (array): The occurrences of a recurring series, if the event is a series master. This property includes occurrences that are part of the recurrence pattern, and exceptions modified, but doesn't include occurrences cancelled from the series. Navigation property. Read-only. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the event. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the event. Read-only. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "allowNewTimeProposals": allowNewTimeProposals,
            "attendees": attendees,
            "body": body,
            "bodyPreview": bodyPreview,
            "end": end,
            "hasAttachments": hasAttachments,
            "hideAttendees": hideAttendees,
            "iCalUId": iCalUId,
            "importance": importance,
            "isAllDay": isAllDay,
            "isCancelled": isCancelled,
            "isDraft": isDraft,
            "isOnlineMeeting": isOnlineMeeting,
            "isOrganizer": isOrganizer,
            "isReminderOn": isReminderOn,
            "location": location,
            "locations": locations,
            "onlineMeeting": onlineMeeting,
            "onlineMeetingProvider": onlineMeetingProvider,
            "onlineMeetingUrl": onlineMeetingUrl,
            "organizer": organizer,
            "originalEndTimeZone": originalEndTimeZone,
            "originalStart": originalStart,
            "originalStartTimeZone": originalStartTimeZone,
            "recurrence": recurrence,
            "reminderMinutesBeforeStart": reminderMinutesBeforeStart,
            "responseRequested": responseRequested,
            "responseStatus": responseStatus,
            "sensitivity": sensitivity,
            "seriesMasterId": seriesMasterId,
            "showAs": showAs,
            "start": start,
            "subject": subject,
            "transactionId": transactionId,
            "type": type,
            "webLink": webLink,
            "attachments": attachments,
            "calendar": calendar,
            "extensions": extensions,
            "instances": instances,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_delete_event(self, user_id: str, event_id: str) -> Any:
        """

        Delete navigation property events for users

        Args:
            user_id (string): user-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_event_list_attachment(
        self,
        user_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_create_attachment(
        self,
        user_id: str,
        event_id: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_get_attachment(
        self,
        user_id: str,
        event_id: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_delete_attachment(
        self, user_id: str, event_id: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_event_attachment_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_attachment_create_upload_session(
        self,
        user_id: str,
        event_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            event_id (string): event-id
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_get_calendar(
        self,
        user_id: str,
        event_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_list_extension(
        self,
        user_id: str,
        event_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_create_extension(
        self, user_id: str, event_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_get_extension(
        self,
        user_id: str,
        event_id: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_update_extension(
        self, user_id: str, event_id: str, extension_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_event_delete_extension(
        self, user_id: str, event_id: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_event_extension_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_list_instance(
        self,
        user_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_get_instance(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        startDateTime: str,
        endDateTime: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get instances from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            startDateTime (string): The start date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T19:00:00-08:00
            endDateTime (string): The end date and time of the time range, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_instance_list_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/attachments"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_instance_create_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        id: Optional[str] = None,
        contentType: Optional[str] = None,
        isInline: Optional[bool] = None,
        lastModifiedDateTime: Optional[str] = None,
        name: Optional[str] = None,
        size: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.
            contentType (string): The MIME type.
            isInline (boolean): true if the attachment is an inline attachment; otherwise, false.
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            name (string): The attachment's file name.
            size (number): The length of the attachment in bytes.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "contentType": contentType,
            "isInline": isInline,
            "lastModifiedDateTime": lastModifiedDateTime,
            "name": name,
            "size": size,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_instance_get_attachment(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_instance_delete_attachment(
        self, user_id: str, event_id: str, event_id1: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_event_instance_attachment_get_count(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_instance_attachment_create_upload_session(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_instance_get_calendar(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get calendar from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/calendar"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_instance_list_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/extensions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_instance_create_extension(
        self, user_id: str, event_id: str, event_id1: str, id: Optional[str] = None
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_instance_get_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_instance_update_extension(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_event_instance_delete_extension(
        self, user_id: str, event_id: str, event_id1: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_event_instance_extension_get_count(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_instance_accept(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_instance_cancel(
        self, user_id: str, event_id: str, event_id1: str, Comment: Optional[str] = None
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_instance_decline(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_instance_dismiss_reminder(
        self, user_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_instance_forward(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_instance_permanent_delete(
        self, user_id: str, event_id: str, event_id1: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_instance_snooze_reminder(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_instance_tentatively_accept(
        self,
        user_id: str,
        event_id: str,
        event_id1: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            event_id1 (string): event-id1
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        if event_id1 is None:
            raise ValueError("Missing required parameter 'event-id1'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/{event_id1}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_instance_get_count(
        self,
        user_id: str,
        event_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            event_id (string): event-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_instance_delta(
        self,
        user_id: str,
        event_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            event_id (string): event-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/instances/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_accept(
        self,
        user_id: str,
        event_id: str,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action accept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"SendResponse": SendResponse, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/microsoft.graph.accept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_cancel(
        self, user_id: str, event_id: str, Comment: Optional[str] = None
    ) -> Any:
        """

        Invoke action cancel

        Args:
            user_id (string): user-id
            event_id (string): event-id
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/microsoft.graph.cancel"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_decline(
        self,
        user_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action decline

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/microsoft.graph.decline"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_dismiss_reminder(self, user_id: str, event_id: str) -> Any:
        """

        Invoke action dismissReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/microsoft.graph.dismissReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_forward(
        self,
        user_id: str,
        event_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ToRecipients (array): ToRecipients
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"ToRecipients": ToRecipients, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_permanent_delete(self, user_id: str, event_id: str) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            event_id (string): event-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_snooze_reminder(
        self,
        user_id: str,
        event_id: str,
        NewReminderTime: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Invoke action snoozeReminder

        Args:
            user_id (string): user-id
            event_id (string): event-id
            NewReminderTime (object): NewReminderTime

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {"NewReminderTime": NewReminderTime}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/microsoft.graph.snoozeReminder"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_tentatively_accept(
        self,
        user_id: str,
        event_id: str,
        ProposedNewTime: Optional[dict[str, dict[str, Any]]] = None,
        SendResponse: Optional[bool] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action tentativelyAccept

        Args:
            user_id (string): user-id
            event_id (string): event-id
            ProposedNewTime (object): ProposedNewTime
            SendResponse (boolean): SendResponse
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if event_id is None:
            raise ValueError("Missing required parameter 'event-id'.")
        request_body_data = None
        request_body_data = {
            "ProposedNewTime": ProposedNewTime,
            "SendResponse": SendResponse,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/{event_id}/microsoft.graph.tentativelyAccept"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_event_get_count(
        self, user_id: str, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_event_delta(
        self,
        user_id: str,
        startDateTime: str,
        endDateTime: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        select: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Invoke function delta

        Args:
            user_id (string): user-id
            startDateTime (string): The start date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            endDateTime (string): The end date and time of the time range in the function, represented in ISO 8601 format. For example, 2019-11-08T20:00:00-08:00
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            select (array): Select properties to be returned
            orderby (array): Order items by property values
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.event
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/events/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("startDateTime", startDateTime),
                ("endDateTime", endDateTime),
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$select", select),
                ("$orderby", orderby),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.user_get_calendar,
            self.user_update_calendar,
            self.user_calendar_list_calendar_permission,
            self.user_calendar_create_calendar_permission,
            self.user_calendar_get_calendar_permission,
            self.user_calendar_update_calendar_permission,
            self.user_calendar_delete_calendar_permission,
            self.user_calendar_calendar_permission_get_count,
            self.user_calendar_list_calendar_view,
            self.user_calendar_get_calendar_view,
            self.user_calendar_calendar_view_list_attachment,
            self.user_calendar_calendar_view_create_attachment,
            self.user_calendar_calendar_view_get_attachment,
            self.user_calendar_calendar_view_delete_attachment,
            self.user_calendar_calendar_view_attachment_get_count,
            self.user_calendar_calendar_view_attachment_create_upload_session,
            self.user_calendar_calendar_view_get_calendar,
            self.user_calendar_calendar_view_list_extension,
            self.user_calendar_calendar_view_create_extension,
            self.user_calendar_calendar_view_get_extension,
            self.user_calendar_calendar_view_update_extension,
            self.user_calendar_calendar_view_delete_extension,
            self.user_calendar_calendar_view_extension_get_count,
            self.user_calendar_calendar_view_list_instance,
            self.user_calendar_calendar_view_get_instance,
            self.user_calendar_calendar_view_instance_list_attachment,
            self.user_calendar_calendar_view_instance_create_attachment,
            self.user_calendar_calendar_view_instance_get_attachment,
            self.user_calendar_calendar_view_instance_delete_attachment,
            self.user_calendar_calendar_view_instance_attachment_get_count,
            self.user_calendar_calendar_view_instance_attachment_create_upload_session,
            self.user_calendar_calendar_view_instance_get_calendar,
            self.user_calendar_calendar_view_instance_list_extension,
            self.user_calendar_calendar_view_instance_create_extension,
            self.user_calendar_calendar_view_instance_get_extension,
            self.user_calendar_calendar_view_instance_update_extension,
            self.user_calendar_calendar_view_instance_delete_extension,
            self.user_calendar_calendar_view_instance_extension_get_count,
            self.user_calendar_calendar_view_instance_accept,
            self.user_calendar_calendar_view_instance_cancel,
            self.user_calendar_calendar_view_instance_decline,
            self.user_calendar_calendar_view_instance_dismiss_reminder,
            self.user_calendar_calendar_view_instance_forward,
            self.user_calendar_calendar_view_instance_permanent_delete,
            self.user_calendar_calendar_view_instance_snooze_reminder,
            self.user_calendar_calendar_view_instance_tentatively_accept,
            self.user_calendar_calendar_view_instance_get_count,
            self.user_calendar_calendar_view_instance_delta,
            self.user_calendar_calendar_view_accept,
            self.user_calendar_calendar_view_cancel,
            self.user_calendar_calendar_view_decline,
            self.user_calendar_calendar_view_dismiss_reminder,
            self.user_calendar_calendar_view_forward,
            self.user_calendar_calendar_view_permanent_delete,
            self.user_calendar_calendar_view_snooze_reminder,
            self.user_calendar_calendar_view_tentatively_accept,
            self.user_calendar_calendar_view_get_count,
            self.user_calendar_calendar_view_delta,
            self.user_calendar_list_event,
            self.user_calendar_create_event,
            self.user_calendar_get_event,
            self.user_calendar_update_event,
            self.user_calendar_delete_event,
            self.user_calendar_event_list_attachment,
            self.user_calendar_event_create_attachment,
            self.user_calendar_event_get_attachment,
            self.user_calendar_event_delete_attachment,
            self.user_calendar_event_attachment_get_count,
            self.user_calendar_event_attachment_create_upload_session,
            self.user_calendar_event_get_calendar,
            self.user_calendar_event_list_extension,
            self.user_calendar_event_create_extension,
            self.user_calendar_event_get_extension,
            self.user_calendar_event_update_extension,
            self.user_calendar_event_delete_extension,
            self.user_calendar_event_extension_get_count,
            self.user_calendar_event_list_instance,
            self.user_calendar_event_get_instance,
            self.user_calendar_event_instance_list_attachment,
            self.user_calendar_event_instance_create_attachment,
            self.user_calendar_event_instance_get_attachment,
            self.user_calendar_event_instance_delete_attachment,
            self.user_calendar_event_instance_attachment_get_count,
            self.user_calendar_event_instance_attachment_create_upload_session,
            self.user_calendar_event_instance_get_calendar,
            self.user_calendar_event_instance_list_extension,
            self.user_calendar_event_instance_create_extension,
            self.user_calendar_event_instance_get_extension,
            self.user_calendar_event_instance_update_extension,
            self.user_calendar_event_instance_delete_extension,
            self.user_calendar_event_instance_extension_get_count,
            self.user_calendar_event_instance_accept,
            self.user_calendar_event_instance_cancel,
            self.user_calendar_event_instance_decline,
            self.user_calendar_event_instance_dismiss_reminder,
            self.user_calendar_event_instance_forward,
            self.user_calendar_event_instance_permanent_delete,
            self.user_calendar_event_instance_snooze_reminder,
            self.user_calendar_event_instance_tentatively_accept,
            self.user_calendar_event_instance_get_count,
            self.user_calendar_event_instance_delta,
            self.user_calendar_event_accept,
            self.user_calendar_event_cancel,
            self.user_calendar_event_decline,
            self.user_calendar_event_dismiss_reminder,
            self.user_calendar_event_forward,
            self.user_calendar_event_permanent_delete,
            self.user_calendar_event_snooze_reminder,
            self.user_calendar_event_tentatively_accept,
            self.user_calendar_event_get_count,
            self.user_calendar_event_delta,
            self.user_calendar_allowed_calendar_sharing_role,
            self.user_calendar_get_schedule,
            self.user_calendar_permanent_delete,
            self.user_list_calendar_group,
            self.user_create_calendar_group,
            self.user_get_calendar_group,
            self.user_update_calendar_group,
            self.user_delete_calendar_group,
            self.user_calendar_group_list_calendar,
            self.user_calendar_group_create_calendar,
            self.user_calendar_group_get_calendar,
            self.user_calendar_group_update_calendar,
            self.user_calendar_group_delete_calendar,
            self.user_calendar_group_calendar_list_calendar_permission,
            self.user_calendar_group_calendar_create_calendar_permission,
            self.user_calendar_group_calendar_get_calendar_permission,
            self.user_calendar_group_calendar_update_calendar_permission,
            self.user_calendar_group_calendar_delete_calendar_permission,
            self.user_calendar_group_calendar_calendar_permission_get_count,
            self.user_calendar_group_calendar_list_calendar_view,
            self.user_calendar_group_calendar_get_calendar_view,
            self.user_calendar_group_calendar_calendar_view_list_attachment,
            self.user_calendar_group_calendar_calendar_view_create_attachment,
            self.user_calendar_group_calendar_calendar_view_get_attachment,
            self.user_calendar_group_calendar_calendar_view_delete_attachment,
            self.user_calendar_group_calendar_calendar_view_attachment_get_count,
            self.user_calendar_group_calendar_calendar_view_attachment_create_upload_session,
            self.user_calendar_group_calendar_calendar_view_get_calendar,
            self.user_calendar_group_calendar_calendar_view_list_extension,
            self.user_calendar_group_calendar_calendar_view_create_extension,
            self.user_calendar_group_calendar_calendar_view_get_extension,
            self.user_calendar_group_calendar_calendar_view_update_extension,
            self.user_calendar_group_calendar_calendar_view_delete_extension,
            self.user_calendar_group_calendar_calendar_view_extension_get_count,
            self.user_calendar_group_calendar_calendar_view_list_instance,
            self.user_calendar_group_calendar_calendar_view_get_instance,
            self.user_calendar_group_calendar_calendar_view_instance_list_attachment,
            self.user_calendar_group_calendar_calendar_view_instance_create_attachment,
            self.user_calendar_group_calendar_calendar_view_instance_get_attachment,
            self.user_calendar_group_calendar_calendar_view_instance_delete_attachment,
            self.user_calendar_group_calendar_calendar_view_instance_attachment_get_count,
            self.user_calendar_group_calendar_calendar_view_instance_attachment_create_upload_session,
            self.user_calendar_group_calendar_calendar_view_instance_get_calendar,
            self.user_calendar_group_calendar_calendar_view_instance_list_extension,
            self.user_calendar_group_calendar_calendar_view_instance_create_extension,
            self.user_calendar_group_calendar_calendar_view_instance_get_extension,
            self.user_calendar_group_calendar_calendar_view_instance_update_extension,
            self.user_calendar_group_calendar_calendar_view_instance_delete_extension,
            self.user_calendar_group_calendar_calendar_view_instance_extension_get_count,
            self.user_calendar_group_calendar_calendar_view_instance_accept,
            self.user_calendar_group_calendar_calendar_view_instance_cancel,
            self.user_calendar_group_calendar_calendar_view_instance_decline,
            self.user_calendar_group_calendar_calendar_view_instance_dismiss_reminder,
            self.user_calendar_group_calendar_calendar_view_instance_forward,
            self.user_calendar_group_calendar_calendar_view_instance_permanent_delete,
            self.user_calendar_group_calendar_calendar_view_instance_snooze_reminder,
            self.user_calendar_group_calendar_calendar_view_instance_tentatively_accept,
            self.user_calendar_group_calendar_calendar_view_instance_get_count,
            self.user_calendar_group_calendar_calendar_view_instance_delta,
            self.user_calendar_group_calendar_calendar_view_accept,
            self.user_calendar_group_calendar_calendar_view_cancel,
            self.user_calendar_group_calendar_calendar_view_decline,
            self.user_calendar_group_calendar_calendar_view_dismiss_reminder,
            self.user_calendar_group_calendar_calendar_view_forward,
            self.user_calendar_group_calendar_calendar_view_permanent_delete,
            self.user_calendar_group_calendar_calendar_view_snooze_reminder,
            self.user_calendar_group_calendar_calendar_view_tentatively_accept,
            self.user_calendar_group_calendar_calendar_view_get_count,
            self.user_calendar_group_calendar_calendar_view_delta,
            self.user_calendar_group_calendar_list_event,
            self.user_calendar_group_calendar_create_event,
            self.user_calendar_group_calendar_get_event,
            self.user_calendar_group_calendar_update_event,
            self.user_calendar_group_calendar_delete_event,
            self.user_calendar_group_calendar_event_list_attachment,
            self.user_calendar_group_calendar_event_create_attachment,
            self.user_calendar_group_calendar_event_get_attachment,
            self.user_calendar_group_calendar_event_delete_attachment,
            self.user_calendar_group_calendar_event_attachment_get_count,
            self.user_calendar_group_calendar_event_attachment_create_upload_session,
            self.user_calendar_group_calendar_event_get_calendar,
            self.user_calendar_group_calendar_event_list_extension,
            self.user_calendar_group_calendar_event_create_extension,
            self.user_calendar_group_calendar_event_get_extension,
            self.user_calendar_group_calendar_event_update_extension,
            self.user_calendar_group_calendar_event_delete_extension,
            self.user_calendar_group_calendar_event_extension_get_count,
            self.user_calendar_group_calendar_event_list_instance,
            self.user_calendar_group_calendar_event_get_instance,
            self.user_calendar_group_calendar_event_instance_list_attachment,
            self.user_calendar_group_calendar_event_instance_create_attachment,
            self.user_calendar_group_calendar_event_instance_get_attachment,
            self.user_calendar_group_calendar_event_instance_delete_attachment,
            self.user_calendar_group_calendar_event_instance_attachment_get_count,
            self.user_calendar_group_calendar_event_instance_attachment_create_upload_session,
            self.user_calendar_group_calendar_event_instance_get_calendar,
            self.user_calendar_group_calendar_event_instance_list_extension,
            self.user_calendar_group_calendar_event_instance_create_extension,
            self.user_calendar_group_calendar_event_instance_get_extension,
            self.user_calendar_group_calendar_event_instance_update_extension,
            self.user_calendar_group_calendar_event_instance_delete_extension,
            self.user_calendar_group_calendar_event_instance_extension_get_count,
            self.user_calendar_group_calendar_event_instance_accept,
            self.user_calendar_group_calendar_event_instance_cancel,
            self.user_calendar_group_calendar_event_instance_decline,
            self.user_calendar_group_calendar_event_instance_dismiss_reminder,
            self.user_calendar_group_calendar_event_instance_forward,
            self.user_calendar_group_calendar_event_instance_permanent_delete,
            self.user_calendar_group_calendar_event_instance_snooze_reminder,
            self.user_calendar_group_calendar_event_instance_tentatively_accept,
            self.user_calendar_group_calendar_event_instance_get_count,
            self.user_calendar_group_calendar_event_instance_delta,
            self.user_calendar_group_calendar_event_accept,
            self.user_calendar_group_calendar_event_cancel,
            self.user_calendar_group_calendar_event_decline,
            self.user_calendar_group_calendar_event_dismiss_reminder,
            self.user_calendar_group_calendar_event_forward,
            self.user_calendar_group_calendar_event_permanent_delete,
            self.user_calendar_group_calendar_event_snooze_reminder,
            self.user_calendar_group_calendar_event_tentatively_accept,
            self.user_calendar_group_calendar_event_get_count,
            self.user_calendar_group_calendar_event_delta,
            self.user_calendar_group_calendar_allowed_calendar_sharing_role,
            self.user_calendar_group_calendar_get_schedule,
            self.user_calendar_group_calendar_permanent_delete,
            self.user_calendar_group_calendar_get_count,
            self.user_calendar_group_get_count,
            self.user_list_calendar,
            self.user_create_calendar,
            self.user_get_calendar,
            self.user_update_calendar,
            self.user_delete_calendar,
            self.user_calendar_list_calendar_permission,
            self.user_calendar_create_calendar_permission,
            self.user_calendar_get_calendar_permission,
            self.user_calendar_update_calendar_permission,
            self.user_calendar_delete_calendar_permission,
            self.user_calendar_calendar_permission_get_count,
            self.user_calendar_list_calendar_view,
            self.user_calendar_get_calendar_view,
            self.user_calendar_calendar_view_list_attachment,
            self.user_calendar_calendar_view_create_attachment,
            self.user_calendar_calendar_view_get_attachment,
            self.user_calendar_calendar_view_delete_attachment,
            self.user_calendar_calendar_view_attachment_get_count,
            self.user_calendar_calendar_view_attachment_create_upload_session,
            self.user_calendar_calendar_view_get_calendar,
            self.user_calendar_calendar_view_list_extension,
            self.user_calendar_calendar_view_create_extension,
            self.user_calendar_calendar_view_get_extension,
            self.user_calendar_calendar_view_update_extension,
            self.user_calendar_calendar_view_delete_extension,
            self.user_calendar_calendar_view_extension_get_count,
            self.user_calendar_calendar_view_list_instance,
            self.user_calendar_calendar_view_get_instance,
            self.user_calendar_calendar_view_instance_list_attachment,
            self.user_calendar_calendar_view_instance_create_attachment,
            self.user_calendar_calendar_view_instance_get_attachment,
            self.user_calendar_calendar_view_instance_delete_attachment,
            self.user_calendar_calendar_view_instance_attachment_get_count,
            self.user_calendar_calendar_view_instance_attachment_create_upload_session,
            self.user_calendar_calendar_view_instance_get_calendar,
            self.user_calendar_calendar_view_instance_list_extension,
            self.user_calendar_calendar_view_instance_create_extension,
            self.user_calendar_calendar_view_instance_get_extension,
            self.user_calendar_calendar_view_instance_update_extension,
            self.user_calendar_calendar_view_instance_delete_extension,
            self.user_calendar_calendar_view_instance_extension_get_count,
            self.user_calendar_calendar_view_instance_accept,
            self.user_calendar_calendar_view_instance_cancel,
            self.user_calendar_calendar_view_instance_decline,
            self.user_calendar_calendar_view_instance_dismiss_reminder,
            self.user_calendar_calendar_view_instance_forward,
            self.user_calendar_calendar_view_instance_permanent_delete,
            self.user_calendar_calendar_view_instance_snooze_reminder,
            self.user_calendar_calendar_view_instance_tentatively_accept,
            self.user_calendar_calendar_view_instance_get_count,
            self.user_calendar_calendar_view_instance_delta,
            self.user_calendar_calendar_view_accept,
            self.user_calendar_calendar_view_cancel,
            self.user_calendar_calendar_view_decline,
            self.user_calendar_calendar_view_dismiss_reminder,
            self.user_calendar_calendar_view_forward,
            self.user_calendar_calendar_view_permanent_delete,
            self.user_calendar_calendar_view_snooze_reminder,
            self.user_calendar_calendar_view_tentatively_accept,
            self.user_calendar_calendar_view_get_count,
            self.user_calendar_calendar_view_delta,
            self.user_calendar_list_event,
            self.user_calendar_create_event,
            self.user_calendar_get_event,
            self.user_calendar_update_event,
            self.user_calendar_delete_event,
            self.user_calendar_event_list_attachment,
            self.user_calendar_event_create_attachment,
            self.user_calendar_event_get_attachment,
            self.user_calendar_event_delete_attachment,
            self.user_calendar_event_attachment_get_count,
            self.user_calendar_event_attachment_create_upload_session,
            self.user_calendar_event_get_calendar,
            self.user_calendar_event_list_extension,
            self.user_calendar_event_create_extension,
            self.user_calendar_event_get_extension,
            self.user_calendar_event_update_extension,
            self.user_calendar_event_delete_extension,
            self.user_calendar_event_extension_get_count,
            self.user_calendar_event_list_instance,
            self.user_calendar_event_get_instance,
            self.user_calendar_event_instance_list_attachment,
            self.user_calendar_event_instance_create_attachment,
            self.user_calendar_event_instance_get_attachment,
            self.user_calendar_event_instance_delete_attachment,
            self.user_calendar_event_instance_attachment_get_count,
            self.user_calendar_event_instance_attachment_create_upload_session,
            self.user_calendar_event_instance_get_calendar,
            self.user_calendar_event_instance_list_extension,
            self.user_calendar_event_instance_create_extension,
            self.user_calendar_event_instance_get_extension,
            self.user_calendar_event_instance_update_extension,
            self.user_calendar_event_instance_delete_extension,
            self.user_calendar_event_instance_extension_get_count,
            self.user_calendar_event_instance_accept,
            self.user_calendar_event_instance_cancel,
            self.user_calendar_event_instance_decline,
            self.user_calendar_event_instance_dismiss_reminder,
            self.user_calendar_event_instance_forward,
            self.user_calendar_event_instance_permanent_delete,
            self.user_calendar_event_instance_snooze_reminder,
            self.user_calendar_event_instance_tentatively_accept,
            self.user_calendar_event_instance_get_count,
            self.user_calendar_event_instance_delta,
            self.user_calendar_event_accept,
            self.user_calendar_event_cancel,
            self.user_calendar_event_decline,
            self.user_calendar_event_dismiss_reminder,
            self.user_calendar_event_forward,
            self.user_calendar_event_permanent_delete,
            self.user_calendar_event_snooze_reminder,
            self.user_calendar_event_tentatively_accept,
            self.user_calendar_event_get_count,
            self.user_calendar_event_delta,
            self.user_calendar_allowed_calendar_sharing_role,
            self.user_calendar_get_schedule,
            self.user_calendar_permanent_delete,
            self.user_calendar_get_count,
            self.user_list_calendar_view,
            self.user_get_calendar_view,
            self.user_calendar_view_list_attachment,
            self.user_calendar_view_create_attachment,
            self.user_calendar_view_get_attachment,
            self.user_calendar_view_delete_attachment,
            self.user_calendar_view_attachment_get_count,
            self.user_calendar_view_attachment_create_upload_session,
            self.user_calendar_view_get_calendar,
            self.user_calendar_view_list_extension,
            self.user_calendar_view_create_extension,
            self.user_calendar_view_get_extension,
            self.user_calendar_view_update_extension,
            self.user_calendar_view_delete_extension,
            self.user_calendar_view_extension_get_count,
            self.user_calendar_view_list_instance,
            self.user_calendar_view_get_instance,
            self.user_calendar_view_instance_list_attachment,
            self.user_calendar_view_instance_create_attachment,
            self.user_calendar_view_instance_get_attachment,
            self.user_calendar_view_instance_delete_attachment,
            self.user_calendar_view_instance_attachment_get_count,
            self.user_calendar_view_instance_attachment_create_upload_session,
            self.user_calendar_view_instance_get_calendar,
            self.user_calendar_view_instance_list_extension,
            self.user_calendar_view_instance_create_extension,
            self.user_calendar_view_instance_get_extension,
            self.user_calendar_view_instance_update_extension,
            self.user_calendar_view_instance_delete_extension,
            self.user_calendar_view_instance_extension_get_count,
            self.user_calendar_view_instance_accept,
            self.user_calendar_view_instance_cancel,
            self.user_calendar_view_instance_decline,
            self.user_calendar_view_instance_dismiss_reminder,
            self.user_calendar_view_instance_forward,
            self.user_calendar_view_instance_permanent_delete,
            self.user_calendar_view_instance_snooze_reminder,
            self.user_calendar_view_instance_tentatively_accept,
            self.user_calendar_view_instance_get_count,
            self.user_calendar_view_instance_delta,
            self.user_calendar_view_accept,
            self.user_calendar_view_cancel,
            self.user_calendar_view_decline,
            self.user_calendar_view_dismiss_reminder,
            self.user_calendar_view_forward,
            self.user_calendar_view_permanent_delete,
            self.user_calendar_view_snooze_reminder,
            self.user_calendar_view_tentatively_accept,
            self.user_calendar_view_get_count,
            self.user_calendar_view_delta,
            self.user_list_event,
            self.user_create_event,
            self.user_get_event,
            self.user_update_event,
            self.user_delete_event,
            self.user_event_list_attachment,
            self.user_event_create_attachment,
            self.user_event_get_attachment,
            self.user_event_delete_attachment,
            self.user_event_attachment_get_count,
            self.user_event_attachment_create_upload_session,
            self.user_event_get_calendar,
            self.user_event_list_extension,
            self.user_event_create_extension,
            self.user_event_get_extension,
            self.user_event_update_extension,
            self.user_event_delete_extension,
            self.user_event_extension_get_count,
            self.user_event_list_instance,
            self.user_event_get_instance,
            self.user_event_instance_list_attachment,
            self.user_event_instance_create_attachment,
            self.user_event_instance_get_attachment,
            self.user_event_instance_delete_attachment,
            self.user_event_instance_attachment_get_count,
            self.user_event_instance_attachment_create_upload_session,
            self.user_event_instance_get_calendar,
            self.user_event_instance_list_extension,
            self.user_event_instance_create_extension,
            self.user_event_instance_get_extension,
            self.user_event_instance_update_extension,
            self.user_event_instance_delete_extension,
            self.user_event_instance_extension_get_count,
            self.user_event_instance_accept,
            self.user_event_instance_cancel,
            self.user_event_instance_decline,
            self.user_event_instance_dismiss_reminder,
            self.user_event_instance_forward,
            self.user_event_instance_permanent_delete,
            self.user_event_instance_snooze_reminder,
            self.user_event_instance_tentatively_accept,
            self.user_event_instance_get_count,
            self.user_event_instance_delta,
            self.user_event_accept,
            self.user_event_cancel,
            self.user_event_decline,
            self.user_event_dismiss_reminder,
            self.user_event_forward,
            self.user_event_permanent_delete,
            self.user_event_snooze_reminder,
            self.user_event_tentatively_accept,
            self.user_event_get_count,
            self.user_event_delta,
        ]
