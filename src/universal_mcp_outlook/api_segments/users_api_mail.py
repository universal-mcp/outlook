from typing import Any, List, Optional
from .api_segment_base import APISegmentBase


class UsersApiMail(APISegmentBase):

    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def user_get_inference_classification(
        self,
        user_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get inferenceClassification from users

        Args:
            user_id (string): user-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.inferenceClassification
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/inferenceClassification"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_update_inference_classification(
        self,
        user_id: str,
        id: Optional[str] = None,
        overrides: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property inferenceClassification in users

        Args:
            user_id (string): user-id
            id (string): The unique identifier for an entity. Read-only.
            overrides (array): A set of overrides for a user to always classify messages from specific senders in certain ways: focused, or other. Read-only. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.inferenceClassification
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        request_body_data = None
        request_body_data = {"id": id, "overrides": overrides}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/inferenceClassification"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_inference_classification_list_override(
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

        Get overrides from users

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
            users.inferenceClassification
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/inferenceClassification/overrides"
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

    def user_inference_classification_create_override(
        self,
        user_id: str,
        id: Optional[str] = None,
        classifyAs: Optional[str] = None,
        senderEmailAddress: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Create new navigation property to overrides for users

        Args:
            user_id (string): user-id
            id (string): The unique identifier for an entity. Read-only.
            classifyAs (string): classifyAs
            senderEmailAddress (object): senderEmailAddress

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.inferenceClassification
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "classifyAs": classifyAs,
            "senderEmailAddress": senderEmailAddress,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/inferenceClassification/overrides"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_inference_classification_get_override(
        self,
        user_id: str,
        inferenceClassificationOverride_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get overrides from users

        Args:
            user_id (string): user-id
            inferenceClassificationOverride_id (string): inferenceClassificationOverride-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.inferenceClassification
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if inferenceClassificationOverride_id is None:
            raise ValueError(
                "Missing required parameter 'inferenceClassificationOverride-id'."
            )
        url = f"{self.main_app_client.base_url}/users/{user_id}/inferenceClassification/overrides/{inferenceClassificationOverride_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_inference_classification_update_override(
        self,
        user_id: str,
        inferenceClassificationOverride_id: str,
        id: Optional[str] = None,
        classifyAs: Optional[str] = None,
        senderEmailAddress: Optional[dict[str, dict[str, Any]]] = None,
    ) -> Any:
        """

        Update the navigation property overrides in users

        Args:
            user_id (string): user-id
            inferenceClassificationOverride_id (string): inferenceClassificationOverride-id
            id (string): The unique identifier for an entity. Read-only.
            classifyAs (string): classifyAs
            senderEmailAddress (object): senderEmailAddress

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.inferenceClassification
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if inferenceClassificationOverride_id is None:
            raise ValueError(
                "Missing required parameter 'inferenceClassificationOverride-id'."
            )
        request_body_data = None
        request_body_data = {
            "id": id,
            "classifyAs": classifyAs,
            "senderEmailAddress": senderEmailAddress,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/inferenceClassification/overrides/{inferenceClassificationOverride_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_inference_classification_delete_override(
        self, user_id: str, inferenceClassificationOverride_id: str
    ) -> Any:
        """

        Delete navigation property overrides for users

        Args:
            user_id (string): user-id
            inferenceClassificationOverride_id (string): inferenceClassificationOverride-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.inferenceClassification
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if inferenceClassificationOverride_id is None:
            raise ValueError(
                "Missing required parameter 'inferenceClassificationOverride-id'."
            )
        url = f"{self.main_app_client.base_url}/users/{user_id}/inferenceClassification/overrides/{inferenceClassificationOverride_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_inference_classification_override_get_count(
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
            users.inferenceClassification
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/inferenceClassification/overrides/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_list_mail_folder(
        self,
        user_id: str,
        includeHiddenFolders: Optional[str] = None,
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

        Get mailFolders from users

        Args:
            user_id (string): user-id
            includeHiddenFolders (string): Include Hidden Folders
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders"
        query_params = {
            k: v
            for k, v in [
                ("includeHiddenFolders", includeHiddenFolders),
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

    def user_create_mail_folder(
        self,
        user_id: str,
        id: Optional[str] = None,
        childFolderCount: Optional[float] = None,
        displayName: Optional[str] = None,
        isHidden: Optional[bool] = None,
        parentFolderId: Optional[str] = None,
        totalItemCount: Optional[float] = None,
        unreadItemCount: Optional[float] = None,
        childFolders: Optional[List[Any]] = None,
        messageRules: Optional[List[Any]] = None,
        messages: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to mailFolders for users

        Args:
            user_id (string): user-id
            id (string): The unique identifier for an entity. Read-only.
            childFolderCount (number): The number of immediate child mailFolders in the current mailFolder.
            displayName (string): The mailFolder's display name.
            isHidden (boolean): Indicates whether the mailFolder is hidden. This property can be set only when creating the folder. Find more information in Hidden mail folders.
            parentFolderId (string): The unique identifier for the mailFolder's parent mailFolder.
            totalItemCount (number): The number of items in the mailFolder.
            unreadItemCount (number): The number of items in the mailFolder marked as unread.
            childFolders (array): The collection of child folders in the mailFolder.
            messageRules (array): The collection of rules that apply to the user's Inbox folder.
            messages (array): The collection of messages in the mailFolder.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "childFolderCount": childFolderCount,
            "displayName": displayName,
            "isHidden": isHidden,
            "parentFolderId": parentFolderId,
            "totalItemCount": totalItemCount,
            "unreadItemCount": unreadItemCount,
            "childFolders": childFolders,
            "messageRules": messageRules,
            "messages": messages,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_get_mail_folder(
        self,
        user_id: str,
        mailFolder_id: str,
        includeHiddenFolders: Optional[str] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get mailFolders from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            includeHiddenFolders (string): Include Hidden Folders
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}"
        query_params = {
            k: v
            for k, v in [
                ("includeHiddenFolders", includeHiddenFolders),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_update_mail_folder(
        self,
        user_id: str,
        mailFolder_id: str,
        id: Optional[str] = None,
        childFolderCount: Optional[float] = None,
        displayName: Optional[str] = None,
        isHidden: Optional[bool] = None,
        parentFolderId: Optional[str] = None,
        totalItemCount: Optional[float] = None,
        unreadItemCount: Optional[float] = None,
        childFolders: Optional[List[Any]] = None,
        messageRules: Optional[List[Any]] = None,
        messages: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property mailFolders in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            id (string): The unique identifier for an entity. Read-only.
            childFolderCount (number): The number of immediate child mailFolders in the current mailFolder.
            displayName (string): The mailFolder's display name.
            isHidden (boolean): Indicates whether the mailFolder is hidden. This property can be set only when creating the folder. Find more information in Hidden mail folders.
            parentFolderId (string): The unique identifier for the mailFolder's parent mailFolder.
            totalItemCount (number): The number of items in the mailFolder.
            unreadItemCount (number): The number of items in the mailFolder marked as unread.
            childFolders (array): The collection of child folders in the mailFolder.
            messageRules (array): The collection of rules that apply to the user's Inbox folder.
            messages (array): The collection of messages in the mailFolder.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "childFolderCount": childFolderCount,
            "displayName": displayName,
            "isHidden": isHidden,
            "parentFolderId": parentFolderId,
            "totalItemCount": totalItemCount,
            "unreadItemCount": unreadItemCount,
            "childFolders": childFolders,
            "messageRules": messageRules,
            "messages": messages,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_delete_mail_folder(self, user_id: str, mailFolder_id: str) -> Any:
        """

        Delete navigation property mailFolders for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_list_child_folder(
        self,
        user_id: str,
        mailFolder_id: str,
        includeHiddenFolders: Optional[str] = None,
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

        Get childFolders from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            includeHiddenFolders (string): Include Hidden Folders
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders"
        query_params = {
            k: v
            for k, v in [
                ("includeHiddenFolders", includeHiddenFolders),
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

    def user_mail_folder_create_child_folder(
        self,
        user_id: str,
        mailFolder_id: str,
        id: Optional[str] = None,
        childFolderCount: Optional[float] = None,
        displayName: Optional[str] = None,
        isHidden: Optional[bool] = None,
        parentFolderId: Optional[str] = None,
        totalItemCount: Optional[float] = None,
        unreadItemCount: Optional[float] = None,
        childFolders: Optional[List[Any]] = None,
        messageRules: Optional[List[Any]] = None,
        messages: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to childFolders for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            id (string): The unique identifier for an entity. Read-only.
            childFolderCount (number): The number of immediate child mailFolders in the current mailFolder.
            displayName (string): The mailFolder's display name.
            isHidden (boolean): Indicates whether the mailFolder is hidden. This property can be set only when creating the folder. Find more information in Hidden mail folders.
            parentFolderId (string): The unique identifier for the mailFolder's parent mailFolder.
            totalItemCount (number): The number of items in the mailFolder.
            unreadItemCount (number): The number of items in the mailFolder marked as unread.
            childFolders (array): The collection of child folders in the mailFolder.
            messageRules (array): The collection of rules that apply to the user's Inbox folder.
            messages (array): The collection of messages in the mailFolder.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "childFolderCount": childFolderCount,
            "displayName": displayName,
            "isHidden": isHidden,
            "parentFolderId": parentFolderId,
            "totalItemCount": totalItemCount,
            "unreadItemCount": unreadItemCount,
            "childFolders": childFolders,
            "messageRules": messageRules,
            "messages": messages,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_get_child_folder(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        includeHiddenFolders: Optional[str] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get childFolders from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            includeHiddenFolders (string): Include Hidden Folders
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}"
        query_params = {
            k: v
            for k, v in [
                ("includeHiddenFolders", includeHiddenFolders),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_update_child_folder(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        id: Optional[str] = None,
        childFolderCount: Optional[float] = None,
        displayName: Optional[str] = None,
        isHidden: Optional[bool] = None,
        parentFolderId: Optional[str] = None,
        totalItemCount: Optional[float] = None,
        unreadItemCount: Optional[float] = None,
        childFolders: Optional[List[Any]] = None,
        messageRules: Optional[List[Any]] = None,
        messages: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property childFolders in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            id (string): The unique identifier for an entity. Read-only.
            childFolderCount (number): The number of immediate child mailFolders in the current mailFolder.
            displayName (string): The mailFolder's display name.
            isHidden (boolean): Indicates whether the mailFolder is hidden. This property can be set only when creating the folder. Find more information in Hidden mail folders.
            parentFolderId (string): The unique identifier for the mailFolder's parent mailFolder.
            totalItemCount (number): The number of items in the mailFolder.
            unreadItemCount (number): The number of items in the mailFolder marked as unread.
            childFolders (array): The collection of child folders in the mailFolder.
            messageRules (array): The collection of rules that apply to the user's Inbox folder.
            messages (array): The collection of messages in the mailFolder.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "childFolderCount": childFolderCount,
            "displayName": displayName,
            "isHidden": isHidden,
            "parentFolderId": parentFolderId,
            "totalItemCount": totalItemCount,
            "unreadItemCount": unreadItemCount,
            "childFolders": childFolders,
            "messageRules": messageRules,
            "messages": messages,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_delete_child_folder(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str
    ) -> Any:
        """

        Delete navigation property childFolders for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_list_message_rule(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
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

        Get messageRules from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messageRules"
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

    def user_mail_folder_child_folder_create_message_rule(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        id: Optional[str] = None,
        actions: Optional[dict[str, dict[str, Any]]] = None,
        conditions: Optional[dict[str, dict[str, Any]]] = None,
        displayName: Optional[str] = None,
        exceptions: Optional[dict[str, dict[str, Any]]] = None,
        hasError: Optional[bool] = None,
        isEnabled: Optional[bool] = None,
        isReadOnly: Optional[bool] = None,
        sequence: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to messageRules for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            id (string): The unique identifier for an entity. Read-only.
            actions (object): actions
            conditions (object): conditions
            displayName (string): The display name of the rule.
            exceptions (object): exceptions
            hasError (boolean): Indicates whether the rule is in an error condition. Read-only.
            isEnabled (boolean): Indicates whether the rule is enabled to be applied to messages.
            isReadOnly (boolean): Indicates if the rule is read-only and cannot be modified or deleted by the rules REST API.
            sequence (number): Indicates the order in which the rule is executed, among other rules.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "actions": actions,
            "conditions": conditions,
            "displayName": displayName,
            "exceptions": exceptions,
            "hasError": hasError,
            "isEnabled": isEnabled,
            "isReadOnly": isReadOnly,
            "sequence": sequence,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messageRules"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_get_message_rule(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        messageRule_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get messageRules from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            messageRule_id (string): messageRule-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if messageRule_id is None:
            raise ValueError("Missing required parameter 'messageRule-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messageRules/{messageRule_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_update_message_rule(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        messageRule_id: str,
        id: Optional[str] = None,
        actions: Optional[dict[str, dict[str, Any]]] = None,
        conditions: Optional[dict[str, dict[str, Any]]] = None,
        displayName: Optional[str] = None,
        exceptions: Optional[dict[str, dict[str, Any]]] = None,
        hasError: Optional[bool] = None,
        isEnabled: Optional[bool] = None,
        isReadOnly: Optional[bool] = None,
        sequence: Optional[float] = None,
    ) -> Any:
        """

        Update the navigation property messageRules in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            messageRule_id (string): messageRule-id
            id (string): The unique identifier for an entity. Read-only.
            actions (object): actions
            conditions (object): conditions
            displayName (string): The display name of the rule.
            exceptions (object): exceptions
            hasError (boolean): Indicates whether the rule is in an error condition. Read-only.
            isEnabled (boolean): Indicates whether the rule is enabled to be applied to messages.
            isReadOnly (boolean): Indicates if the rule is read-only and cannot be modified or deleted by the rules REST API.
            sequence (number): Indicates the order in which the rule is executed, among other rules.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if messageRule_id is None:
            raise ValueError("Missing required parameter 'messageRule-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "actions": actions,
            "conditions": conditions,
            "displayName": displayName,
            "exceptions": exceptions,
            "hasError": hasError,
            "isEnabled": isEnabled,
            "isReadOnly": isReadOnly,
            "sequence": sequence,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messageRules/{messageRule_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_delete_message_rule(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str, messageRule_id: str
    ) -> Any:
        """

        Delete navigation property messageRules for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            messageRule_id (string): messageRule-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if messageRule_id is None:
            raise ValueError("Missing required parameter 'messageRule-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messageRules/{messageRule_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_rule_get_count(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messageRules/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_list_message(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
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

        Get messages from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages"
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

    def user_mail_folder_child_folder_create_message(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        bccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        ccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        conversationId: Optional[str] = None,
        conversationIndex: Optional[str] = None,
        flag: Optional[dict[str, dict[str, Any]]] = None,
        from_: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        importance: Optional[str] = None,
        inferenceClassification: Optional[str] = None,
        internetMessageHeaders: Optional[List[dict[str, dict[str, Any]]]] = None,
        internetMessageId: Optional[str] = None,
        isDeliveryReceiptRequested: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isRead: Optional[bool] = None,
        isReadReceiptRequested: Optional[bool] = None,
        parentFolderId: Optional[str] = None,
        receivedDateTime: Optional[str] = None,
        replyTo: Optional[List[dict[str, dict[str, Any]]]] = None,
        sender: Optional[dict[str, dict[str, Any]]] = None,
        sentDateTime: Optional[str] = None,
        subject: Optional[str] = None,
        toRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        uniqueBody: Optional[dict[str, dict[str, Any]]] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        extensions: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to messages for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            bccRecipients (array): The Bcc: recipients for the message.
            body (object): body
            bodyPreview (string): The first 255 characters of the message body. It is in text format.
            ccRecipients (array): The Cc: recipients for the message.
            conversationId (string): The ID of the conversation the email belongs to.
            conversationIndex (string): Indicates the position of the message within the conversation.
            flag (object): flag
            from_ (object): from
            hasAttachments (boolean): Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as <IMG src='cid:image001.jpg@01D26CD8.6C05F070'>.
            importance (string): importance
            inferenceClassification (string): inferenceClassification
            internetMessageHeaders (array): A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.
            internetMessageId (string): The message ID in the format specified by RFC2822.
            isDeliveryReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            isDraft (boolean): Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.
            isRead (boolean): Indicates whether the message has been read.
            isReadReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            parentFolderId (string): The unique identifier for the message's parent mailFolder.
            receivedDateTime (string): The date and time the message was received.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            replyTo (array): The email addresses to use when replying.
            sender (object): sender
            sentDateTime (string): The date and time the message was sent.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            subject (string): The subject of the message.
            toRecipients (array): The To: recipients for the message.
            uniqueBody (object): uniqueBody
            webLink (string): The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, the browser shows the message in the Outlook on the web review pane.The message opens in the browser if you are signed in to your mailbox via Outlook on the web. You are prompted to sign in if you are not already signed in with the browser.This URL cannot be accessed from within an iFrame.
            attachments (array): The fileAttachment and itemAttachment attachments for the message.
            extensions (array): The collection of open extensions defined for the message. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the message. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the message. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "bccRecipients": bccRecipients,
            "body": body,
            "bodyPreview": bodyPreview,
            "ccRecipients": ccRecipients,
            "conversationId": conversationId,
            "conversationIndex": conversationIndex,
            "flag": flag,
            "from": from_,
            "hasAttachments": hasAttachments,
            "importance": importance,
            "inferenceClassification": inferenceClassification,
            "internetMessageHeaders": internetMessageHeaders,
            "internetMessageId": internetMessageId,
            "isDeliveryReceiptRequested": isDeliveryReceiptRequested,
            "isDraft": isDraft,
            "isRead": isRead,
            "isReadReceiptRequested": isReadReceiptRequested,
            "parentFolderId": parentFolderId,
            "receivedDateTime": receivedDateTime,
            "replyTo": replyTo,
            "sender": sender,
            "sentDateTime": sentDateTime,
            "subject": subject,
            "toRecipients": toRecipients,
            "uniqueBody": uniqueBody,
            "webLink": webLink,
            "attachments": attachments,
            "extensions": extensions,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_get_message(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get messages from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_update_message(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        bccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        ccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        conversationId: Optional[str] = None,
        conversationIndex: Optional[str] = None,
        flag: Optional[dict[str, dict[str, Any]]] = None,
        from_: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        importance: Optional[str] = None,
        inferenceClassification: Optional[str] = None,
        internetMessageHeaders: Optional[List[dict[str, dict[str, Any]]]] = None,
        internetMessageId: Optional[str] = None,
        isDeliveryReceiptRequested: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isRead: Optional[bool] = None,
        isReadReceiptRequested: Optional[bool] = None,
        parentFolderId: Optional[str] = None,
        receivedDateTime: Optional[str] = None,
        replyTo: Optional[List[dict[str, dict[str, Any]]]] = None,
        sender: Optional[dict[str, dict[str, Any]]] = None,
        sentDateTime: Optional[str] = None,
        subject: Optional[str] = None,
        toRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        uniqueBody: Optional[dict[str, dict[str, Any]]] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        extensions: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property messages in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            bccRecipients (array): The Bcc: recipients for the message.
            body (object): body
            bodyPreview (string): The first 255 characters of the message body. It is in text format.
            ccRecipients (array): The Cc: recipients for the message.
            conversationId (string): The ID of the conversation the email belongs to.
            conversationIndex (string): Indicates the position of the message within the conversation.
            flag (object): flag
            from_ (object): from
            hasAttachments (boolean): Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as <IMG src='cid:image001.jpg@01D26CD8.6C05F070'>.
            importance (string): importance
            inferenceClassification (string): inferenceClassification
            internetMessageHeaders (array): A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.
            internetMessageId (string): The message ID in the format specified by RFC2822.
            isDeliveryReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            isDraft (boolean): Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.
            isRead (boolean): Indicates whether the message has been read.
            isReadReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            parentFolderId (string): The unique identifier for the message's parent mailFolder.
            receivedDateTime (string): The date and time the message was received.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            replyTo (array): The email addresses to use when replying.
            sender (object): sender
            sentDateTime (string): The date and time the message was sent.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            subject (string): The subject of the message.
            toRecipients (array): The To: recipients for the message.
            uniqueBody (object): uniqueBody
            webLink (string): The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, the browser shows the message in the Outlook on the web review pane.The message opens in the browser if you are signed in to your mailbox via Outlook on the web. You are prompted to sign in if you are not already signed in with the browser.This URL cannot be accessed from within an iFrame.
            attachments (array): The fileAttachment and itemAttachment attachments for the message.
            extensions (array): The collection of open extensions defined for the message. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the message. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the message. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "bccRecipients": bccRecipients,
            "body": body,
            "bodyPreview": bodyPreview,
            "ccRecipients": ccRecipients,
            "conversationId": conversationId,
            "conversationIndex": conversationIndex,
            "flag": flag,
            "from": from_,
            "hasAttachments": hasAttachments,
            "importance": importance,
            "inferenceClassification": inferenceClassification,
            "internetMessageHeaders": internetMessageHeaders,
            "internetMessageId": internetMessageId,
            "isDeliveryReceiptRequested": isDeliveryReceiptRequested,
            "isDraft": isDraft,
            "isRead": isRead,
            "isReadReceiptRequested": isReadReceiptRequested,
            "parentFolderId": parentFolderId,
            "receivedDateTime": receivedDateTime,
            "replyTo": replyTo,
            "sender": sender,
            "sentDateTime": sentDateTime,
            "subject": subject,
            "toRecipients": toRecipients,
            "uniqueBody": uniqueBody,
            "webLink": webLink,
            "attachments": attachments,
            "extensions": extensions,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_delete_message(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str, message_id: str
    ) -> Any:
        """

        Delete navigation property messages for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_get_messages_content(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str, message_id: str
    ) -> Any:
        """

        Get media content for the navigation property messages from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id

        Returns:
            Any: Retrieved media content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/$value"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_set_messages_content(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        body_content: bytes,
    ) -> Any:
        """

        Update media content for the navigation property messages in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            body_content (bytes | None): Raw binary content for the request body.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = body_content
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/$value"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/octet-stream",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_delete_messages_content(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str, message_id: str
    ) -> Any:
        """

        Delete media content for the navigation property messages in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/$value"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_list_attachment(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
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
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/attachments"
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

    def user_mail_folder_child_folder_message_create_attachment(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
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
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
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
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_get_attachment(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_delete_attachment(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        attachment_id: str,
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_attachment_get_count(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_attachment_create_upload_session(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_list_extension(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
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
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/extensions"
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

    def user_mail_folder_child_folder_message_create_extension(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_get_extension(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_update_extension(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_delete_extension(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        extension_id: str,
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_extension_get_count(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_copy(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        DestinationId: Optional[str] = None,
    ) -> Any:
        """

        Invoke action copy

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            DestinationId (string): DestinationId

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"DestinationId": DestinationId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/microsoft.graph.copy"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_create_forward(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action createForward

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            ToRecipients (array): ToRecipients
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {
            "ToRecipients": ToRecipients,
            "Message": Message,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/microsoft.graph.createForward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_create_reply(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action createReply

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/microsoft.graph.createReply"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_create_reply_all(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action createReplyAll

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/microsoft.graph.createReplyAll"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_forward(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            ToRecipients (array): ToRecipients
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {
            "ToRecipients": ToRecipients,
            "Message": Message,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_move(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        DestinationId: Optional[str] = None,
    ) -> Any:
        """

        Invoke action move

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            DestinationId (string): DestinationId

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"DestinationId": DestinationId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/microsoft.graph.move"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_permanent_delete(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str, message_id: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_reply(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action reply

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/microsoft.graph.reply"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_reply_all(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action replyAll

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/microsoft.graph.replyAll"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_send(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str, message_id: str
    ) -> Any:
        """

        Invoke action send

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/{message_id}/microsoft.graph.send"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_get_count(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_message_delta(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        changeType: Optional[str] = None,
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
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            changeType (string): A custom query option to filter the delta response based on the type of change. Supported values are created, updated or deleted.
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/messages/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("changeType", changeType),
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

    def user_mail_folder_child_folder_copy(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        DestinationId: Optional[str] = None,
    ) -> Any:
        """

        Invoke action copy

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            DestinationId (string): DestinationId

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        request_body_data = None
        request_body_data = {"DestinationId": DestinationId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/microsoft.graph.copy"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_move(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        DestinationId: Optional[str] = None,
    ) -> Any:
        """

        Invoke action move

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1
            DestinationId (string): DestinationId

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        request_body_data = None
        request_body_data = {"DestinationId": DestinationId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/microsoft.graph.move"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_permanent_delete(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            mailFolder_id1 (string): mailFolder-id1

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if mailFolder_id1 is None:
            raise ValueError("Missing required parameter 'mailFolder-id1'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/{mailFolder_id1}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_child_folder_get_count(
        self,
        user_id: str,
        mailFolder_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_child_folder_delta(
        self,
        user_id: str,
        mailFolder_id: str,
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
            mailFolder_id (string): mailFolder-id
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/childFolders/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
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

    def user_mail_folder_list_message_rule(
        self,
        user_id: str,
        mailFolder_id: str,
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

        Get messageRules from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messageRules"
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

    def user_mail_folder_create_message_rule(
        self,
        user_id: str,
        mailFolder_id: str,
        id: Optional[str] = None,
        actions: Optional[dict[str, dict[str, Any]]] = None,
        conditions: Optional[dict[str, dict[str, Any]]] = None,
        displayName: Optional[str] = None,
        exceptions: Optional[dict[str, dict[str, Any]]] = None,
        hasError: Optional[bool] = None,
        isEnabled: Optional[bool] = None,
        isReadOnly: Optional[bool] = None,
        sequence: Optional[float] = None,
    ) -> Any:
        """

        Create new navigation property to messageRules for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            id (string): The unique identifier for an entity. Read-only.
            actions (object): actions
            conditions (object): conditions
            displayName (string): The display name of the rule.
            exceptions (object): exceptions
            hasError (boolean): Indicates whether the rule is in an error condition. Read-only.
            isEnabled (boolean): Indicates whether the rule is enabled to be applied to messages.
            isReadOnly (boolean): Indicates if the rule is read-only and cannot be modified or deleted by the rules REST API.
            sequence (number): Indicates the order in which the rule is executed, among other rules.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "actions": actions,
            "conditions": conditions,
            "displayName": displayName,
            "exceptions": exceptions,
            "hasError": hasError,
            "isEnabled": isEnabled,
            "isReadOnly": isReadOnly,
            "sequence": sequence,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messageRules"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_get_message_rule(
        self,
        user_id: str,
        mailFolder_id: str,
        messageRule_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get messageRules from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            messageRule_id (string): messageRule-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if messageRule_id is None:
            raise ValueError("Missing required parameter 'messageRule-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messageRules/{messageRule_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_update_message_rule(
        self,
        user_id: str,
        mailFolder_id: str,
        messageRule_id: str,
        id: Optional[str] = None,
        actions: Optional[dict[str, dict[str, Any]]] = None,
        conditions: Optional[dict[str, dict[str, Any]]] = None,
        displayName: Optional[str] = None,
        exceptions: Optional[dict[str, dict[str, Any]]] = None,
        hasError: Optional[bool] = None,
        isEnabled: Optional[bool] = None,
        isReadOnly: Optional[bool] = None,
        sequence: Optional[float] = None,
    ) -> Any:
        """

        Update the navigation property messageRules in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            messageRule_id (string): messageRule-id
            id (string): The unique identifier for an entity. Read-only.
            actions (object): actions
            conditions (object): conditions
            displayName (string): The display name of the rule.
            exceptions (object): exceptions
            hasError (boolean): Indicates whether the rule is in an error condition. Read-only.
            isEnabled (boolean): Indicates whether the rule is enabled to be applied to messages.
            isReadOnly (boolean): Indicates if the rule is read-only and cannot be modified or deleted by the rules REST API.
            sequence (number): Indicates the order in which the rule is executed, among other rules.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if messageRule_id is None:
            raise ValueError("Missing required parameter 'messageRule-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "actions": actions,
            "conditions": conditions,
            "displayName": displayName,
            "exceptions": exceptions,
            "hasError": hasError,
            "isEnabled": isEnabled,
            "isReadOnly": isReadOnly,
            "sequence": sequence,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messageRules/{messageRule_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_delete_message_rule(
        self, user_id: str, mailFolder_id: str, messageRule_id: str
    ) -> Any:
        """

        Delete navigation property messageRules for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            messageRule_id (string): messageRule-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if messageRule_id is None:
            raise ValueError("Missing required parameter 'messageRule-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messageRules/{messageRule_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_message_rule_get_count(
        self,
        user_id: str,
        mailFolder_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messageRules/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_list_message(
        self,
        user_id: str,
        mailFolder_id: str,
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

        Get messages from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages"
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

    def user_mail_folder_create_message(
        self,
        user_id: str,
        mailFolder_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        bccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        ccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        conversationId: Optional[str] = None,
        conversationIndex: Optional[str] = None,
        flag: Optional[dict[str, dict[str, Any]]] = None,
        from_: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        importance: Optional[str] = None,
        inferenceClassification: Optional[str] = None,
        internetMessageHeaders: Optional[List[dict[str, dict[str, Any]]]] = None,
        internetMessageId: Optional[str] = None,
        isDeliveryReceiptRequested: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isRead: Optional[bool] = None,
        isReadReceiptRequested: Optional[bool] = None,
        parentFolderId: Optional[str] = None,
        receivedDateTime: Optional[str] = None,
        replyTo: Optional[List[dict[str, dict[str, Any]]]] = None,
        sender: Optional[dict[str, dict[str, Any]]] = None,
        sentDateTime: Optional[str] = None,
        subject: Optional[str] = None,
        toRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        uniqueBody: Optional[dict[str, dict[str, Any]]] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        extensions: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to messages for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            bccRecipients (array): The Bcc: recipients for the message.
            body (object): body
            bodyPreview (string): The first 255 characters of the message body. It is in text format.
            ccRecipients (array): The Cc: recipients for the message.
            conversationId (string): The ID of the conversation the email belongs to.
            conversationIndex (string): Indicates the position of the message within the conversation.
            flag (object): flag
            from_ (object): from
            hasAttachments (boolean): Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as <IMG src='cid:image001.jpg@01D26CD8.6C05F070'>.
            importance (string): importance
            inferenceClassification (string): inferenceClassification
            internetMessageHeaders (array): A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.
            internetMessageId (string): The message ID in the format specified by RFC2822.
            isDeliveryReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            isDraft (boolean): Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.
            isRead (boolean): Indicates whether the message has been read.
            isReadReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            parentFolderId (string): The unique identifier for the message's parent mailFolder.
            receivedDateTime (string): The date and time the message was received.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            replyTo (array): The email addresses to use when replying.
            sender (object): sender
            sentDateTime (string): The date and time the message was sent.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            subject (string): The subject of the message.
            toRecipients (array): The To: recipients for the message.
            uniqueBody (object): uniqueBody
            webLink (string): The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, the browser shows the message in the Outlook on the web review pane.The message opens in the browser if you are signed in to your mailbox via Outlook on the web. You are prompted to sign in if you are not already signed in with the browser.This URL cannot be accessed from within an iFrame.
            attachments (array): The fileAttachment and itemAttachment attachments for the message.
            extensions (array): The collection of open extensions defined for the message. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the message. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the message. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "bccRecipients": bccRecipients,
            "body": body,
            "bodyPreview": bodyPreview,
            "ccRecipients": ccRecipients,
            "conversationId": conversationId,
            "conversationIndex": conversationIndex,
            "flag": flag,
            "from": from_,
            "hasAttachments": hasAttachments,
            "importance": importance,
            "inferenceClassification": inferenceClassification,
            "internetMessageHeaders": internetMessageHeaders,
            "internetMessageId": internetMessageId,
            "isDeliveryReceiptRequested": isDeliveryReceiptRequested,
            "isDraft": isDraft,
            "isRead": isRead,
            "isReadReceiptRequested": isReadReceiptRequested,
            "parentFolderId": parentFolderId,
            "receivedDateTime": receivedDateTime,
            "replyTo": replyTo,
            "sender": sender,
            "sentDateTime": sentDateTime,
            "subject": subject,
            "toRecipients": toRecipients,
            "uniqueBody": uniqueBody,
            "webLink": webLink,
            "attachments": attachments,
            "extensions": extensions,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_get_message(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get messages from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_update_message(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        bccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        ccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        conversationId: Optional[str] = None,
        conversationIndex: Optional[str] = None,
        flag: Optional[dict[str, dict[str, Any]]] = None,
        from_: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        importance: Optional[str] = None,
        inferenceClassification: Optional[str] = None,
        internetMessageHeaders: Optional[List[dict[str, dict[str, Any]]]] = None,
        internetMessageId: Optional[str] = None,
        isDeliveryReceiptRequested: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isRead: Optional[bool] = None,
        isReadReceiptRequested: Optional[bool] = None,
        parentFolderId: Optional[str] = None,
        receivedDateTime: Optional[str] = None,
        replyTo: Optional[List[dict[str, dict[str, Any]]]] = None,
        sender: Optional[dict[str, dict[str, Any]]] = None,
        sentDateTime: Optional[str] = None,
        subject: Optional[str] = None,
        toRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        uniqueBody: Optional[dict[str, dict[str, Any]]] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        extensions: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property messages in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            bccRecipients (array): The Bcc: recipients for the message.
            body (object): body
            bodyPreview (string): The first 255 characters of the message body. It is in text format.
            ccRecipients (array): The Cc: recipients for the message.
            conversationId (string): The ID of the conversation the email belongs to.
            conversationIndex (string): Indicates the position of the message within the conversation.
            flag (object): flag
            from_ (object): from
            hasAttachments (boolean): Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as <IMG src='cid:image001.jpg@01D26CD8.6C05F070'>.
            importance (string): importance
            inferenceClassification (string): inferenceClassification
            internetMessageHeaders (array): A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.
            internetMessageId (string): The message ID in the format specified by RFC2822.
            isDeliveryReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            isDraft (boolean): Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.
            isRead (boolean): Indicates whether the message has been read.
            isReadReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            parentFolderId (string): The unique identifier for the message's parent mailFolder.
            receivedDateTime (string): The date and time the message was received.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            replyTo (array): The email addresses to use when replying.
            sender (object): sender
            sentDateTime (string): The date and time the message was sent.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            subject (string): The subject of the message.
            toRecipients (array): The To: recipients for the message.
            uniqueBody (object): uniqueBody
            webLink (string): The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, the browser shows the message in the Outlook on the web review pane.The message opens in the browser if you are signed in to your mailbox via Outlook on the web. You are prompted to sign in if you are not already signed in with the browser.This URL cannot be accessed from within an iFrame.
            attachments (array): The fileAttachment and itemAttachment attachments for the message.
            extensions (array): The collection of open extensions defined for the message. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the message. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the message. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "bccRecipients": bccRecipients,
            "body": body,
            "bodyPreview": bodyPreview,
            "ccRecipients": ccRecipients,
            "conversationId": conversationId,
            "conversationIndex": conversationIndex,
            "flag": flag,
            "from": from_,
            "hasAttachments": hasAttachments,
            "importance": importance,
            "inferenceClassification": inferenceClassification,
            "internetMessageHeaders": internetMessageHeaders,
            "internetMessageId": internetMessageId,
            "isDeliveryReceiptRequested": isDeliveryReceiptRequested,
            "isDraft": isDraft,
            "isRead": isRead,
            "isReadReceiptRequested": isReadReceiptRequested,
            "parentFolderId": parentFolderId,
            "receivedDateTime": receivedDateTime,
            "replyTo": replyTo,
            "sender": sender,
            "sentDateTime": sentDateTime,
            "subject": subject,
            "toRecipients": toRecipients,
            "uniqueBody": uniqueBody,
            "webLink": webLink,
            "attachments": attachments,
            "extensions": extensions,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_delete_message(
        self, user_id: str, mailFolder_id: str, message_id: str
    ) -> Any:
        """

        Delete navigation property messages for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_get_messages_content(
        self, user_id: str, mailFolder_id: str, message_id: str
    ) -> Any:
        """

        Get media content for the navigation property messages from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id

        Returns:
            Any: Retrieved media content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/$value"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_set_messages_content(
        self, user_id: str, mailFolder_id: str, message_id: str, body_content: bytes
    ) -> Any:
        """

        Update media content for the navigation property messages in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            body_content (bytes | None): Raw binary content for the request body.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = body_content
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/$value"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/octet-stream",
        )
        return self._handle_response(response)

    def user_mail_folder_delete_messages_content(
        self, user_id: str, mailFolder_id: str, message_id: str
    ) -> Any:
        """

        Delete media content for the navigation property messages in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/$value"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_message_list_attachment(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
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
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/attachments"
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

    def user_mail_folder_message_create_attachment(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
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
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
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
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_get_attachment(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_message_delete_attachment(
        self, user_id: str, mailFolder_id: str, message_id: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_message_attachment_get_count(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_message_attachment_create_upload_session(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_list_extension(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
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
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/extensions"
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

    def user_mail_folder_message_create_extension(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_get_extension(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_message_update_extension(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_message_delete_extension(
        self, user_id: str, mailFolder_id: str, message_id: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_message_extension_get_count(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_message_copy(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        DestinationId: Optional[str] = None,
    ) -> Any:
        """

        Invoke action copy

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            DestinationId (string): DestinationId

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"DestinationId": DestinationId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/microsoft.graph.copy"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_create_forward(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action createForward

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            ToRecipients (array): ToRecipients
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {
            "ToRecipients": ToRecipients,
            "Message": Message,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/microsoft.graph.createForward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_create_reply(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action createReply

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/microsoft.graph.createReply"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_create_reply_all(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action createReplyAll

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/microsoft.graph.createReplyAll"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_forward(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            ToRecipients (array): ToRecipients
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {
            "ToRecipients": ToRecipients,
            "Message": Message,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_move(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        DestinationId: Optional[str] = None,
    ) -> Any:
        """

        Invoke action move

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            DestinationId (string): DestinationId

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"DestinationId": DestinationId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/microsoft.graph.move"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_permanent_delete(
        self, user_id: str, mailFolder_id: str, message_id: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_reply(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action reply

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/microsoft.graph.reply"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_reply_all(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action replyAll

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/microsoft.graph.replyAll"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_send(
        self, user_id: str, mailFolder_id: str, message_id: str
    ) -> Any:
        """

        Invoke action send

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/{message_id}/microsoft.graph.send"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_message_get_count(
        self,
        user_id: str,
        mailFolder_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_message_delta(
        self,
        user_id: str,
        mailFolder_id: str,
        changeType: Optional[str] = None,
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
            mailFolder_id (string): mailFolder-id
            changeType (string): A custom query option to filter the delta response based on the type of change. Supported values are created, updated or deleted.
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/messages/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("changeType", changeType),
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

    def user_mail_folder_copy(
        self, user_id: str, mailFolder_id: str, DestinationId: Optional[str] = None
    ) -> Any:
        """

        Invoke action copy

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            DestinationId (string): DestinationId

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        request_body_data = None
        request_body_data = {"DestinationId": DestinationId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/microsoft.graph.copy"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_move(
        self, user_id: str, mailFolder_id: str, DestinationId: Optional[str] = None
    ) -> Any:
        """

        Invoke action move

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id
            DestinationId (string): DestinationId

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        request_body_data = None
        request_body_data = {"DestinationId": DestinationId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/microsoft.graph.move"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_permanent_delete(
        self, user_id: str, mailFolder_id: str
    ) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            mailFolder_id (string): mailFolder-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if mailFolder_id is None:
            raise ValueError("Missing required parameter 'mailFolder-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/{mailFolder_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_mail_folder_get_count(
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_mail_folder_delta(
        self,
        user_id: str,
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
            users.mailFolder
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/mailFolders/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
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

    def user_list_message(
        self,
        user_id: str,
        includeHiddenMessages: Optional[str] = None,
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

        Get messages from users

        Args:
            user_id (string): user-id
            includeHiddenMessages (string): Include Hidden Messages
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
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages"
        query_params = {
            k: v
            for k, v in [
                ("includeHiddenMessages", includeHiddenMessages),
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

    def user_create_message(
        self,
        user_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        bccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        ccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        conversationId: Optional[str] = None,
        conversationIndex: Optional[str] = None,
        flag: Optional[dict[str, dict[str, Any]]] = None,
        from_: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        importance: Optional[str] = None,
        inferenceClassification: Optional[str] = None,
        internetMessageHeaders: Optional[List[dict[str, dict[str, Any]]]] = None,
        internetMessageId: Optional[str] = None,
        isDeliveryReceiptRequested: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isRead: Optional[bool] = None,
        isReadReceiptRequested: Optional[bool] = None,
        parentFolderId: Optional[str] = None,
        receivedDateTime: Optional[str] = None,
        replyTo: Optional[List[dict[str, dict[str, Any]]]] = None,
        sender: Optional[dict[str, dict[str, Any]]] = None,
        sentDateTime: Optional[str] = None,
        subject: Optional[str] = None,
        toRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        uniqueBody: Optional[dict[str, dict[str, Any]]] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        extensions: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Create new navigation property to messages for users

        Args:
            user_id (string): user-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            bccRecipients (array): The Bcc: recipients for the message.
            body (object): body
            bodyPreview (string): The first 255 characters of the message body. It is in text format.
            ccRecipients (array): The Cc: recipients for the message.
            conversationId (string): The ID of the conversation the email belongs to.
            conversationIndex (string): Indicates the position of the message within the conversation.
            flag (object): flag
            from_ (object): from
            hasAttachments (boolean): Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as <IMG src='cid:image001.jpg@01D26CD8.6C05F070'>.
            importance (string): importance
            inferenceClassification (string): inferenceClassification
            internetMessageHeaders (array): A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.
            internetMessageId (string): The message ID in the format specified by RFC2822.
            isDeliveryReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            isDraft (boolean): Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.
            isRead (boolean): Indicates whether the message has been read.
            isReadReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            parentFolderId (string): The unique identifier for the message's parent mailFolder.
            receivedDateTime (string): The date and time the message was received.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            replyTo (array): The email addresses to use when replying.
            sender (object): sender
            sentDateTime (string): The date and time the message was sent.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            subject (string): The subject of the message.
            toRecipients (array): The To: recipients for the message.
            uniqueBody (object): uniqueBody
            webLink (string): The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, the browser shows the message in the Outlook on the web review pane.The message opens in the browser if you are signed in to your mailbox via Outlook on the web. You are prompted to sign in if you are not already signed in with the browser.This URL cannot be accessed from within an iFrame.
            attachments (array): The fileAttachment and itemAttachment attachments for the message.
            extensions (array): The collection of open extensions defined for the message. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the message. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the message. Nullable.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
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
            "bccRecipients": bccRecipients,
            "body": body,
            "bodyPreview": bodyPreview,
            "ccRecipients": ccRecipients,
            "conversationId": conversationId,
            "conversationIndex": conversationIndex,
            "flag": flag,
            "from": from_,
            "hasAttachments": hasAttachments,
            "importance": importance,
            "inferenceClassification": inferenceClassification,
            "internetMessageHeaders": internetMessageHeaders,
            "internetMessageId": internetMessageId,
            "isDeliveryReceiptRequested": isDeliveryReceiptRequested,
            "isDraft": isDraft,
            "isRead": isRead,
            "isReadReceiptRequested": isReadReceiptRequested,
            "parentFolderId": parentFolderId,
            "receivedDateTime": receivedDateTime,
            "replyTo": replyTo,
            "sender": sender,
            "sentDateTime": sentDateTime,
            "subject": subject,
            "toRecipients": toRecipients,
            "uniqueBody": uniqueBody,
            "webLink": webLink,
            "attachments": attachments,
            "extensions": extensions,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_get_message(
        self,
        user_id: str,
        message_id: str,
        includeHiddenMessages: Optional[str] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get messages from users

        Args:
            user_id (string): user-id
            message_id (string): message-id
            includeHiddenMessages (string): Include Hidden Messages
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}"
        query_params = {
            k: v
            for k, v in [
                ("includeHiddenMessages", includeHiddenMessages),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_update_message(
        self,
        user_id: str,
        message_id: str,
        id: Optional[str] = None,
        categories: Optional[List[str]] = None,
        changeKey: Optional[str] = None,
        createdDateTime: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        bccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        body: Optional[dict[str, dict[str, Any]]] = None,
        bodyPreview: Optional[str] = None,
        ccRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        conversationId: Optional[str] = None,
        conversationIndex: Optional[str] = None,
        flag: Optional[dict[str, dict[str, Any]]] = None,
        from_: Optional[dict[str, dict[str, Any]]] = None,
        hasAttachments: Optional[bool] = None,
        importance: Optional[str] = None,
        inferenceClassification: Optional[str] = None,
        internetMessageHeaders: Optional[List[dict[str, dict[str, Any]]]] = None,
        internetMessageId: Optional[str] = None,
        isDeliveryReceiptRequested: Optional[bool] = None,
        isDraft: Optional[bool] = None,
        isRead: Optional[bool] = None,
        isReadReceiptRequested: Optional[bool] = None,
        parentFolderId: Optional[str] = None,
        receivedDateTime: Optional[str] = None,
        replyTo: Optional[List[dict[str, dict[str, Any]]]] = None,
        sender: Optional[dict[str, dict[str, Any]]] = None,
        sentDateTime: Optional[str] = None,
        subject: Optional[str] = None,
        toRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        uniqueBody: Optional[dict[str, dict[str, Any]]] = None,
        webLink: Optional[str] = None,
        attachments: Optional[List[Any]] = None,
        extensions: Optional[List[Any]] = None,
        multiValueExtendedProperties: Optional[List[Any]] = None,
        singleValueExtendedProperties: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property messages in users

        Args:
            user_id (string): user-id
            message_id (string): message-id
            id (string): The unique identifier for an entity. Read-only.
            categories (array): The categories associated with the item
            changeKey (string): Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
            createdDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            lastModifiedDateTime (string): The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
            bccRecipients (array): The Bcc: recipients for the message.
            body (object): body
            bodyPreview (string): The first 255 characters of the message body. It is in text format.
            ccRecipients (array): The Cc: recipients for the message.
            conversationId (string): The ID of the conversation the email belongs to.
            conversationIndex (string): Indicates the position of the message within the conversation.
            flag (object): flag
            from_ (object): from
            hasAttachments (boolean): Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as <IMG src='cid:image001.jpg@01D26CD8.6C05F070'>.
            importance (string): importance
            inferenceClassification (string): inferenceClassification
            internetMessageHeaders (array): A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.
            internetMessageId (string): The message ID in the format specified by RFC2822.
            isDeliveryReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            isDraft (boolean): Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.
            isRead (boolean): Indicates whether the message has been read.
            isReadReceiptRequested (boolean): Indicates whether a read receipt is requested for the message.
            parentFolderId (string): The unique identifier for the message's parent mailFolder.
            receivedDateTime (string): The date and time the message was received.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            replyTo (array): The email addresses to use when replying.
            sender (object): sender
            sentDateTime (string): The date and time the message was sent.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
            subject (string): The subject of the message.
            toRecipients (array): The To: recipients for the message.
            uniqueBody (object): uniqueBody
            webLink (string): The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, the browser shows the message in the Outlook on the web review pane.The message opens in the browser if you are signed in to your mailbox via Outlook on the web. You are prompted to sign in if you are not already signed in with the browser.This URL cannot be accessed from within an iFrame.
            attachments (array): The fileAttachment and itemAttachment attachments for the message.
            extensions (array): The collection of open extensions defined for the message. Nullable.
            multiValueExtendedProperties (array): The collection of multi-value extended properties defined for the message. Nullable.
            singleValueExtendedProperties (array): The collection of single-value extended properties defined for the message. Nullable.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "categories": categories,
            "changeKey": changeKey,
            "createdDateTime": createdDateTime,
            "lastModifiedDateTime": lastModifiedDateTime,
            "bccRecipients": bccRecipients,
            "body": body,
            "bodyPreview": bodyPreview,
            "ccRecipients": ccRecipients,
            "conversationId": conversationId,
            "conversationIndex": conversationIndex,
            "flag": flag,
            "from": from_,
            "hasAttachments": hasAttachments,
            "importance": importance,
            "inferenceClassification": inferenceClassification,
            "internetMessageHeaders": internetMessageHeaders,
            "internetMessageId": internetMessageId,
            "isDeliveryReceiptRequested": isDeliveryReceiptRequested,
            "isDraft": isDraft,
            "isRead": isRead,
            "isReadReceiptRequested": isReadReceiptRequested,
            "parentFolderId": parentFolderId,
            "receivedDateTime": receivedDateTime,
            "replyTo": replyTo,
            "sender": sender,
            "sentDateTime": sentDateTime,
            "subject": subject,
            "toRecipients": toRecipients,
            "uniqueBody": uniqueBody,
            "webLink": webLink,
            "attachments": attachments,
            "extensions": extensions,
            "multiValueExtendedProperties": multiValueExtendedProperties,
            "singleValueExtendedProperties": singleValueExtendedProperties,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_delete_message(self, user_id: str, message_id: str) -> Any:
        """

        Delete navigation property messages for users

        Args:
            user_id (string): user-id
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_get_messages_content(self, user_id: str, message_id: str) -> Any:
        """

        Get media content for the navigation property messages from users

        Args:
            user_id (string): user-id
            message_id (string): message-id

        Returns:
            Any: Retrieved media content

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/$value"
        query_params = {}
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_set_messages_content(
        self, user_id: str, message_id: str, body_content: bytes
    ) -> Any:
        """

        Update media content for the navigation property messages in users

        Args:
            user_id (string): user-id
            message_id (string): message-id
            body_content (bytes | None): Raw binary content for the request body.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = body_content
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/$value"
        query_params = {}
        response = self._put(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/octet-stream",
        )
        return self._handle_response(response)

    def user_delete_messages_content(self, user_id: str, message_id: str) -> Any:
        """

        Delete media content for the navigation property messages in users

        Args:
            user_id (string): user-id
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/$value"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_message_list_attachment(
        self,
        user_id: str,
        message_id: str,
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
            message_id (string): message-id
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
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/attachments"
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

    def user_message_create_attachment(
        self,
        user_id: str,
        message_id: str,
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
            message_id (string): message-id
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
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
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
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/attachments"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_get_attachment(
        self,
        user_id: str,
        message_id: str,
        attachment_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get attachments from users

        Args:
            user_id (string): user-id
            message_id (string): message-id
            attachment_id (string): attachment-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/attachments/{attachment_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_message_delete_attachment(
        self, user_id: str, message_id: str, attachment_id: str
    ) -> Any:
        """

        Delete navigation property attachments for users

        Args:
            user_id (string): user-id
            message_id (string): message-id
            attachment_id (string): attachment-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if attachment_id is None:
            raise ValueError("Missing required parameter 'attachment-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/attachments/{attachment_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_message_attachment_get_count(
        self,
        user_id: str,
        message_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            message_id (string): message-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/attachments/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_message_attachment_create_upload_session(
        self,
        user_id: str,
        message_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Invoke action createUploadSession

        Args:
            user_id (string): user-id
            message_id (string): message-id
            AttachmentItem (object): AttachmentItem

        Returns:
            dict[str, Any]: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"AttachmentItem": AttachmentItem}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/attachments/microsoft.graph.createUploadSession"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_list_extension(
        self,
        user_id: str,
        message_id: str,
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
            message_id (string): message-id
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
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/extensions"
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

    def user_message_create_extension(
        self, user_id: str, message_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Create new navigation property to extensions for users

        Args:
            user_id (string): user-id
            message_id (string): message-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/extensions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_get_extension(
        self,
        user_id: str,
        message_id: str,
        extension_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get extensions from users

        Args:
            user_id (string): user-id
            message_id (string): message-id
            extension_id (string): extension-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/extensions/{extension_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_message_update_extension(
        self, user_id: str, message_id: str, extension_id: str, id: Optional[str] = None
    ) -> Any:
        """

        Update the navigation property extensions in users

        Args:
            user_id (string): user-id
            message_id (string): message-id
            extension_id (string): extension-id
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        request_body_data = None
        request_body_data = {"id": id}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/extensions/{extension_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def user_message_delete_extension(
        self, user_id: str, message_id: str, extension_id: str
    ) -> Any:
        """

        Delete navigation property extensions for users

        Args:
            user_id (string): user-id
            message_id (string): message-id
            extension_id (string): extension-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        if extension_id is None:
            raise ValueError("Missing required parameter 'extension-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/extensions/{extension_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def user_message_extension_get_count(
        self,
        user_id: str,
        message_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            user_id (string): user-id
            message_id (string): message-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/extensions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_message_copy(
        self, user_id: str, message_id: str, DestinationId: Optional[str] = None
    ) -> Any:
        """

        Invoke action copy

        Args:
            user_id (string): user-id
            message_id (string): message-id
            DestinationId (string): DestinationId

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"DestinationId": DestinationId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/microsoft.graph.copy"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_create_forward(
        self,
        user_id: str,
        message_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action createForward

        Args:
            user_id (string): user-id
            message_id (string): message-id
            ToRecipients (array): ToRecipients
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {
            "ToRecipients": ToRecipients,
            "Message": Message,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/microsoft.graph.createForward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_create_reply(
        self,
        user_id: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action createReply

        Args:
            user_id (string): user-id
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/microsoft.graph.createReply"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_create_reply_all(
        self,
        user_id: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action createReplyAll

        Args:
            user_id (string): user-id
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/microsoft.graph.createReplyAll"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_forward(
        self,
        user_id: str,
        message_id: str,
        ToRecipients: Optional[List[dict[str, dict[str, Any]]]] = None,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action forward

        Args:
            user_id (string): user-id
            message_id (string): message-id
            ToRecipients (array): ToRecipients
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {
            "ToRecipients": ToRecipients,
            "Message": Message,
            "Comment": Comment,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/microsoft.graph.forward"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_move(
        self, user_id: str, message_id: str, DestinationId: Optional[str] = None
    ) -> Any:
        """

        Invoke action move

        Args:
            user_id (string): user-id
            message_id (string): message-id
            DestinationId (string): DestinationId

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"DestinationId": DestinationId}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/microsoft.graph.move"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_permanent_delete(self, user_id: str, message_id: str) -> Any:
        """

        Invoke action permanentDelete

        Args:
            user_id (string): user-id
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/microsoft.graph.permanentDelete"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_reply(
        self,
        user_id: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action reply

        Args:
            user_id (string): user-id
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/microsoft.graph.reply"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_reply_all(
        self,
        user_id: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Invoke action replyAll

        Args:
            user_id (string): user-id
            message_id (string): message-id
            Message (string): Message
            Comment (string): Comment

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        request_body_data = {"Message": Message, "Comment": Comment}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/microsoft.graph.replyAll"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_send(self, user_id: str, message_id: str) -> Any:
        """

        Invoke action send

        Args:
            user_id (string): user-id
            message_id (string): message-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        if message_id is None:
            raise ValueError("Missing required parameter 'message-id'.")
        request_body_data = None
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/{message_id}/microsoft.graph.send"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def user_message_get_count(
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
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def user_message_delta(
        self,
        user_id: str,
        changeType: Optional[str] = None,
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
            changeType (string): A custom query option to filter the delta response based on the type of change. Supported values are created, updated or deleted.
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
            users.message
        """
        if user_id is None:
            raise ValueError("Missing required parameter 'user-id'.")
        url = f"{self.main_app_client.base_url}/users/{user_id}/messages/microsoft.graph.delta()"
        query_params = {
            k: v
            for k, v in [
                ("changeType", changeType),
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
            self.user_get_inference_classification,
            self.user_update_inference_classification,
            self.user_inference_classification_list_override,
            self.user_inference_classification_create_override,
            self.user_inference_classification_get_override,
            self.user_inference_classification_update_override,
            self.user_inference_classification_delete_override,
            self.user_inference_classification_override_get_count,
            self.user_list_mail_folder,
            self.user_create_mail_folder,
            self.user_get_mail_folder,
            self.user_update_mail_folder,
            self.user_delete_mail_folder,
            self.user_mail_folder_list_child_folder,
            self.user_mail_folder_create_child_folder,
            self.user_mail_folder_get_child_folder,
            self.user_mail_folder_update_child_folder,
            self.user_mail_folder_delete_child_folder,
            self.user_mail_folder_child_folder_list_message_rule,
            self.user_mail_folder_child_folder_create_message_rule,
            self.user_mail_folder_child_folder_get_message_rule,
            self.user_mail_folder_child_folder_update_message_rule,
            self.user_mail_folder_child_folder_delete_message_rule,
            self.user_mail_folder_child_folder_message_rule_get_count,
            self.user_mail_folder_child_folder_list_message,
            self.user_mail_folder_child_folder_create_message,
            self.user_mail_folder_child_folder_get_message,
            self.user_mail_folder_child_folder_update_message,
            self.user_mail_folder_child_folder_delete_message,
            self.user_mail_folder_child_folder_get_messages_content,
            self.user_mail_folder_child_folder_set_messages_content,
            self.user_mail_folder_child_folder_delete_messages_content,
            self.user_mail_folder_child_folder_message_list_attachment,
            self.user_mail_folder_child_folder_message_create_attachment,
            self.user_mail_folder_child_folder_message_get_attachment,
            self.user_mail_folder_child_folder_message_delete_attachment,
            self.user_mail_folder_child_folder_message_attachment_get_count,
            self.user_mail_folder_child_folder_message_attachment_create_upload_session,
            self.user_mail_folder_child_folder_message_list_extension,
            self.user_mail_folder_child_folder_message_create_extension,
            self.user_mail_folder_child_folder_message_get_extension,
            self.user_mail_folder_child_folder_message_update_extension,
            self.user_mail_folder_child_folder_message_delete_extension,
            self.user_mail_folder_child_folder_message_extension_get_count,
            self.user_mail_folder_child_folder_message_copy,
            self.user_mail_folder_child_folder_message_create_forward,
            self.user_mail_folder_child_folder_message_create_reply,
            self.user_mail_folder_child_folder_message_create_reply_all,
            self.user_mail_folder_child_folder_message_forward,
            self.user_mail_folder_child_folder_message_move,
            self.user_mail_folder_child_folder_message_permanent_delete,
            self.user_mail_folder_child_folder_message_reply,
            self.user_mail_folder_child_folder_message_reply_all,
            self.user_mail_folder_child_folder_message_send,
            self.user_mail_folder_child_folder_message_get_count,
            self.user_mail_folder_child_folder_message_delta,
            self.user_mail_folder_child_folder_copy,
            self.user_mail_folder_child_folder_move,
            self.user_mail_folder_child_folder_permanent_delete,
            self.user_mail_folder_child_folder_get_count,
            self.user_mail_folder_child_folder_delta,
            self.user_mail_folder_list_message_rule,
            self.user_mail_folder_create_message_rule,
            self.user_mail_folder_get_message_rule,
            self.user_mail_folder_update_message_rule,
            self.user_mail_folder_delete_message_rule,
            self.user_mail_folder_message_rule_get_count,
            self.user_mail_folder_list_message,
            self.user_mail_folder_create_message,
            self.user_mail_folder_get_message,
            self.user_mail_folder_update_message,
            self.user_mail_folder_delete_message,
            self.user_mail_folder_get_messages_content,
            self.user_mail_folder_set_messages_content,
            self.user_mail_folder_delete_messages_content,
            self.user_mail_folder_message_list_attachment,
            self.user_mail_folder_message_create_attachment,
            self.user_mail_folder_message_get_attachment,
            self.user_mail_folder_message_delete_attachment,
            self.user_mail_folder_message_attachment_get_count,
            self.user_mail_folder_message_attachment_create_upload_session,
            self.user_mail_folder_message_list_extension,
            self.user_mail_folder_message_create_extension,
            self.user_mail_folder_message_get_extension,
            self.user_mail_folder_message_update_extension,
            self.user_mail_folder_message_delete_extension,
            self.user_mail_folder_message_extension_get_count,
            self.user_mail_folder_message_copy,
            self.user_mail_folder_message_create_forward,
            self.user_mail_folder_message_create_reply,
            self.user_mail_folder_message_create_reply_all,
            self.user_mail_folder_message_forward,
            self.user_mail_folder_message_move,
            self.user_mail_folder_message_permanent_delete,
            self.user_mail_folder_message_reply,
            self.user_mail_folder_message_reply_all,
            self.user_mail_folder_message_send,
            self.user_mail_folder_message_get_count,
            self.user_mail_folder_message_delta,
            self.user_mail_folder_copy,
            self.user_mail_folder_move,
            self.user_mail_folder_permanent_delete,
            self.user_mail_folder_get_count,
            self.user_mail_folder_delta,
            self.user_list_message,
            self.user_create_message,
            self.user_get_message,
            self.user_update_message,
            self.user_delete_message,
            self.user_get_messages_content,
            self.user_set_messages_content,
            self.user_delete_messages_content,
            self.user_message_list_attachment,
            self.user_message_create_attachment,
            self.user_message_get_attachment,
            self.user_message_delete_attachment,
            self.user_message_attachment_get_count,
            self.user_message_attachment_create_upload_session,
            self.user_message_list_extension,
            self.user_message_create_extension,
            self.user_message_get_extension,
            self.user_message_update_extension,
            self.user_message_delete_extension,
            self.user_message_extension_get_count,
            self.user_message_copy,
            self.user_message_create_forward,
            self.user_message_create_reply,
            self.user_message_create_reply_all,
            self.user_message_forward,
            self.user_message_move,
            self.user_message_permanent_delete,
            self.user_message_reply,
            self.user_message_reply_all,
            self.user_message_send,
            self.user_message_get_count,
            self.user_message_delta,
        ]
