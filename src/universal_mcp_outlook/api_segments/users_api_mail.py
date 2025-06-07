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

        Retrieves inference classification data for a specific user, allowing optional selection and expansion of fields using query parameters.

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

        Updates the inference classification details for a specific user using the PATCH method, applying partial modifications to the existing resource based on the provided JSON body.

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

        Retrieves and lists override classifications for a specific user using the provided parameters for filtering, sorting, and selecting data.

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

        Overrides inference classification settings for a specific user by sending a JSON payload with the updated override details.

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

        Retrieves details of a specific inference classification override for a user by ID, allowing optional selection and expansion of specific fields.

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

        Updates specific properties of an inference classification override for a user using JSON Patch operations.

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

        Deletes a specific inference classification override for a user using the provided user ID and inference classification override ID.

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

    def usr_inf_class_override_count(
        self, user_id: str, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Retrieves the count of inference classification overrides for a specified user ID using optional search and filter parameters.

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

        Retrieves a list of mail folders for a specified user, allowing for optional filtering, sorting, and expansion of results.

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

        Creates a new mail folder for a specified user using the provided JSON body and returns a relevant status response.

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

        Retrieves information about a specific mail folder for a user, optionally including hidden folders and allowing selective expansion of related data.

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

        Updates a specific mail folder for a user by applying partial modifications using a JSON request body.

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

        Deletes a specific mail folder for a user using the "DELETE" method, requiring the user ID and mail folder ID as path parameters and an "If-Match" header for optimistic concurrency control.

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

        Retrieves a list of child folders for a specified mail folder of a user using the "GET" method, allowing optional filtering and sorting through query parameters.

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

        Creates a new child folder within a specified mail folder for a given user using the provided JSON request body.

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

        Retrieves a list of child folders within a specified mail folder for a given user, allowing optional filtering by hidden folders and selection of specific fields.

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

        Updates the properties of a child mail folder within a specified mail folder for a given user using the PATCH method.

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

        Deletes a child mail folder from a specified mail folder for a given user.

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

    def usr_mail_fldr_child_fldr_list_msg_rule(
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

        Retrieves message rules for a child folder in a specific mail folder of a user, supporting filtering, sorting, and optional expansion of related data.

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

    def usr_mail_fldr_child_fldr_create_msg_rule(
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

        Creates a message rule in a specific child folder of a user's mailbox by specifying conditions and actions to be applied to incoming messages.

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

    def usr_mail_fldr_child_fldr_get_msg_rule(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        messageRule_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Retrieves a specific message rule in a mail folder, allowing optional selection and expansion of properties.

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

    def usr_mail_fldr_child_fldr_update_msg_rule(
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

        Updates a specific message rule in a child folder of a user's mail folder using JSON Patch operations.

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

    def usr_mail_fldr_child_fldr_delete_msg_rule(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str, messageRule_id: str
    ) -> Any:
        """

        Deletes a specific message rule from a child folder of a mail folder associated with a user using the DELETE method.

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

    def usr_mail_fldr_child_fldr_msg_rule_count(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Retrieves the count of message rules for a specific child mail folder, identified by `mailFolder-id1`, within a parent mail folder, identified by `mailFolder-id`, belonging to a user with ID `user-id`.

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

        Retrieves a list of messages within a specific child folder of a mail folder for a given user, allowing for filtering, sorting, and expansion of related data.

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

        Creates a new message in a specified child mail folder of a user's mail folder using the provided JSON body.

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

        Retrieves a specific message from a child folder within a mail folder associated with a user's mailbox, allowing optional selection and expansion of properties.

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

        Modifies a specific email message in a nested mail folder using the PATCH method, updating properties as specified in the JSON request body.

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

        Deletes a specific email message identified by the message ID from a child folder within a mail folder of a user's mailbox.

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

    def usr_mail_fldr_child_fldr_get_msgs_content(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str, message_id: str
    ) -> Any:
        """

        Retrieves the content of a specific email message using the specified user ID, mail folder ID, child folder ID, and message ID.

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

    def usr_mail_fldr_child_fldr_set_msgs_content(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        body_content: bytes,
    ) -> Any:
        """

        Updates or replaces a specific email message in a Microsoft Exchange mailbox using its ID, located within a nested folder structure, by sending the message content as a binary stream.

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

    def usr_mail_fldr_child_fldr_delete_msgs_content(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str, message_id: str
    ) -> Any:
        """

        Deletes a message from a specific folder within a user's mailbox using the DELETE method, requiring the user ID, mail folder IDs, and message ID, and optionally an If-Match header for concurrency control.

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

    def usr_mail_fldr_child_fldr_msg_list_attach(
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

        Retrieves an attachment from a specific message in a child folder of a mail folder belonging to a user, optionally allowing filtering, sorting, and selecting specific properties.

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

    def usr_mail_fldr_child_fldr_msg_create_attach(
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

        Adds an attachment to a specific message in a child folder of a mail folder for a user using a JSON payload.

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

    def usr_mail_fldr_child_fldr_msg_get_attach(
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

        Retrieves a specific attachment from a message in a nested mail folder using the "GET" method, allowing optional filtering with `$select` and `$expand` parameters.

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

    def usr_mail_fldr_child_fldr_msg_delete_attach(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        attachment_id: str,
    ) -> Any:
        """

        Deletes an attachment from a message in a child folder of a mail folder belonging to a user using the DELETE method, requiring the user ID, mail folder IDs, message ID, and attachment ID.

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

    def usr_mail_fldr_child_fldr_msg_attach_count(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Retrieves the count of attachments for a specific message in a nested mail folder using the "GET" method.

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

    def usr_mail_fldr_child_fldr_msg_attach_upload(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Creates an upload session to allow attaching a file to a specific message located within a nested mail folder for a user using Microsoft Graph.

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

    def usr_mail_fldr_child_fldr_msg_list_ext(
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

        Retrieves an email message with specified extensions from a specific child folder within a mail folder belonging to a user.

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

    def usr_mail_fldr_child_fldr_msg_create_ext(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Adds a new extension to a specific message in a child folder of a mail folder for a user using the POST method, requiring a JSON body with the extension details.

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

    def usr_mail_fldr_child_fldr_msg_get_ext(
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

        Retrieves the specified extension for a message in a child folder of a mail folder belonging to a user, allowing for optional selection and expansion of specific properties.

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

    def usr_mail_fldr_child_fldr_msg_update_ext(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        extension_id: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Updates an extension of a specific message in a child folder of a mail folder for a user using the PATCH method.

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

    def usr_mail_fldr_child_fldr_msg_delete_ext(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        extension_id: str,
    ) -> Any:
        """

        Deletes an extension with the specified ID from a message in a child folder of a mail folder associated with a user.

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

    def usr_mail_fldr_child_fldr_msg_ext_count(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Retrieves the count of extensions for a specific message in a nested mail folder using the "GET" method.

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

        Copies a message to a folder within a user's mailbox using the Microsoft Graph API.

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

    def usr_mail_fldr_child_fldr_msg_create_forward(
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

        Creates a draft to forward an existing message using the Microsoft Graph API, allowing specification of recipients and content in JSON or MIME format.

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

    def usr_mail_fldr_child_fldr_msg_create_reply(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Creates a draft message to reply to an existing email in a user's mailbox, using either JSON or MIME format, and requires specifying the user ID, mail folder IDs, and the message ID to be replied to.

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

    def usr_mail_fldr_child_fldr_msg_create_reply_all(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Creates a draft message to reply to the sender and all recipients of a specified message using the Microsoft Graph API.

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

        Forwards a specified email message using the Microsoft Graph API by sending a POST request, allowing the message to be forwarded in JSON format with specified recipients and optional comments, and saves the forwarded message in the Sent Items folder.

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

        Moves a message with the specified ID from a child folder to another folder within the same user's mailbox, using the Microsoft Graph API.

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

    def usr_mail_fldr_child_fldr_msg_perm_delete(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str, message_id: str
    ) -> Any:
        """

        Permanently deletes a specified message in a nested mail folder of a user's mailbox using the Microsoft Graph API.

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

        Replies to an email message using the Microsoft Graph API by sending a response from a specific user's mailbox, maintaining the conversation thread.

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

    def usr_mail_fldr_child_fldr_msg_reply_all(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        message_id: str,
        Message: Optional[Any] = None,
        Comment: Optional[str] = None,
    ) -> Any:
        """

        Sends a reply to all recipients of the specified message and saves it in the Sent Items folder[1][4].

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

        Sends the specified email message from a deeply nested mail folder of the user using Microsoft Graph API.

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

    def usr_mail_fldr_child_fldr_msg_count(
        self,
        user_id: str,
        mailFolder_id: str,
        mailFolder_id1: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Retrieves the count of messages within a specific child folder of a user's mail folder using the "GET" method.

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

        Retrieves incremental changes—such as additions, updates, or deletions—to messages in a specified nested mail folder for a given user, supporting optional filtering and pagination parameters[3][1][2].

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

        Copies a child mail folder and its contents to another mail folder within a user's mailbox using the Microsoft Graph API.

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

        Moves a mail folder and its contents to another mail folder using the Microsoft Graph API.

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

    def usr_mail_fldr_child_fldr_perm_delete(
        self, user_id: str, mailFolder_id: str, mailFolder_id1: str
    ) -> Any:
        """

        Permanently deletes a mail folder and its child folder, removing all items from the user's mailbox using the Microsoft Graph API.

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

        Retrieves the count of child folders within a specified mail folder for a user.

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

        Retrieves changes to child folders under a specified mail folder for a user using delta query, allowing applications to track newly created, updated, or deleted child folders without performing a full read of the data.

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

        Retrieves a list of message rules for a specified user and mail folder, supporting optional query parameters for filtering, sorting, and pagination.

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

        Creates a new message rule for a specific mail folder belonging to a user using the provided request body.

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

        Retrieves a specific message rule for a user’s mail folder using the provided user, mail folder, and rule identifiers.

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

        Updates a specific message rule for a given mail folder of a user using a JSON body with operations to modify its properties.

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

        Deletes a specific message rule for a user's mail folder using the DELETE method.

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

        Returns the total count of message rules for a specified mail folder belonging to a given user.

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

        Retrieves a list of messages from a specific mail folder belonging to a user, allowing for filtering, sorting, and selecting specific fields.

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

        Creates a new message in the specified mail folder for the given user.

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

        Retrieves a specific message from a user's mail folder using the provided user ID, mail folder ID, and message ID, optionally selecting specific fields and expanding related data.

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

        Updates a specific email message in a given mail folder for a user, using JSON Patch operations to modify its properties.

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

        Deletes a specific email message from a user's mail folder using the provided user ID, mail folder ID, and message ID.

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

        Retrieves the content of a specific email message from a designated mail folder for a user.

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

        Updates or replaces the content of a specific email message in a user's mailbox using the provided binary data.

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

        Deletes a message from a user's mail folder using the specified message ID, requiring the user ID and mail folder ID for identification.

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

        Retrieves an attachment from a specific message in a mail folder for a user, allowing optional filtering and sorting of the response.

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

        Adds an attachment to a specific message in a mail folder using the provided JSON payload.

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

        Retrieves an attachment by its ID from a specific message in a mail folder belonging to a user, allowing for optional selection and expansion of specific properties.

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

        Deletes an attachment from a specific message in a mail folder of a user, using the specified user ID, mail folder ID, message ID, and attachment ID.

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

        Retrieves the total number of email attachments for a specified message in a user’s mail folder.

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

    def usr_mail_fldr_msg_attach_upload(
        self,
        user_id: str,
        mailFolder_id: str,
        message_id: str,
        AttachmentItem: Optional[dict[str, dict[str, Any]]] = None,
    ) -> dict[str, Any]:
        """

        Creates an upload session to iteratively upload ranges of a file as an attachment to a specified email message in the user's mailbox.

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

        Retrieves and returns extensions for a specific message in a mail folder, allowing for optional filtering, sorting, and expansion of related data.

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

        Adds an extension to a specific message in a mail folder using the provided JSON payload.

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

        Retrieves a specific extension for a message within a mail folder of a user, allowing optional selection and expansion of properties through query parameters.

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

        Updates an extension for a specific message in a mail folder of a user using the PATCH method, with the request body specifying the modifications to apply.

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

        Deletes an extension from a specific message in a mail folder for a given user.

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

        Retrieves the count of message extensions for a specific message in a mail folder belonging to a user.

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

        Copies a message to a specified folder within a user's mailbox using the Microsoft Graph API.

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

        Creates a draft to forward an existing email message by specifying recipients and optional comments or message body content using the Microsoft Graph API.

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

        Creates a draft reply message to the specified email using the Microsoft Graph API.

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

        Creates a draft message to reply to the sender and all recipients of a specified message using the Microsoft Graph API, allowing for customization in either JSON or MIME format.

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

        Forwards an email message using the Microsoft Graph API by specifying the user ID, mail folder ID, and message ID in the path, and providing the recipient details in the request body.

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

        Moves a message from a specified folder to another folder within the same user's mailbox by creating a new copy of the message in the destination folder and removing the original.

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

        Permanently deletes a message from a specified mail folder in a user's mailbox using the Microsoft Graph API, moving it to the Purges folder where it cannot be recovered.

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

        Replies to an email message using the Microsoft Graph API, specifying the user ID, mail folder ID, and message ID, and requiring a JSON body in the request.

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

        Replies to all recipients of a specified email message using the Microsoft Graph API, creating and sending the reply in a single call.

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

        Sends a specified email message from a user’s mail folder using its message ID via the Microsoft Graph API.

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

        Retrieves the count of messages in a specified mail folder for a given user using the GET method.

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

        Tracks changes to messages in a specified mail folder of a user using the Microsoft Graph delta query, allowing retrieval of created, updated, or deleted messages based on optional query parameters such as change type.

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

        Copies a specified mail folder and its contents to another mail folder for a given user using the Microsoft Graph API.

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

        Moves a mail folder and its contents to another mail folder using the Microsoft Graph API.

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

        Permanently deletes a specified mail folder and its items from a user's mailbox using the Microsoft Graph API.

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

        Retrieves the count of mail folders for a specified user using the provided search and filter parameters.

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

        Tracks changes to mail folders for a specified user using the delta function, allowing applications to discover newly created, updated, or deleted entities without performing a full read.

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

        Retrieves a list of messages for a specified user, allowing optional filtering and sorting with query parameters such as includeHiddenMessages, top, skip, search, filter, count, orderby, select, and expand.

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

        Sends a message to a specified user using their ID and returns a status message.

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

        Retrieves a specific message identified by `{message-id}` for a user with `{user-id}`, allowing optional filtering with `includeHiddenMessages`, selection of specific fields with `$select`, and expansion of related data with `$expand`.

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

        Updates a specific message for a user using the provided JSON Patch operations and returns a status message based on the outcome.

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

        Deletes a specific message identified by `message-id` for a user with the specified `user-id`, returning a successful status if the operation is completed.

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

        Retrieves the raw value of a specific message for a specified user.

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

        Updates the content of a specific message identified by `{message-id}` for a user with `{user-id}` using a binary payload.

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

        Deletes a specific message for a user using the provided user ID and message ID, potentially requiring an If-Match header for conditional requests.

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

        Retrieves attachments for a specific message belonging to a user, with optional filtering and sorting capabilities.

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

        Adds a new attachment to a specific message for a user using the provided JSON payload.

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

        Retrieves a specific attachment from a message associated with a user, allowing optional selection and expansion of fields through query parameters.

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

        Deletes an attachment from a specific message belonging to a user using the provided IDs and returns a status message, optionally requiring an "If-Match" header for version control.

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

        Retrieves the number of attachments for a specific message of a user using the GET method.

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

        Creates an upload session to iteratively upload a file as an attachment to a specified Outlook message, returning an upload URL for subsequent file upload operations.

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

        Retrieves message extensions for a specific message belonging to a user, allowing for optional filtering, sorting, and selection of fields.

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

        Adds an extension to a specific message for a given user using the provided JSON data.

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

        Retrieves details about a specific extension for a message associated with a user, allowing optional filtering and expansion of the response using query parameters.

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

        Updates specific properties of an extension within a message for a specified user using the PATCH method, requiring a JSON body with the changes.

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

        Deletes a specific extension from a message identified by its ID associated with a user, using the "DELETE" method.

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

        Retrieves the count of message extensions for a specified message owned by a specific user, optionally filtered or searched according to query parameters.

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

        Copies a message to a folder within the specified user's mailbox using the Microsoft Graph API.

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

        Creates a draft to forward an existing message, allowing specification of recipients and content in either JSON or MIME format, which can be updated and sent in a subsequent operation.

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

        Creates a draft message in JSON format to reply to an existing message using the Microsoft Graph API, allowing the specification of the reply content in the request body.

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

        Creates a draft reply message addressed to the sender and all recipients of the specified message, supporting JSON or MIME format in the request body[1][4].

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

        Forwards an email message using the Microsoft Graph API by specifying the recipient and optionally adding a comment, saving the forwarded message in the Sent Items folder.

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

        Moves a message to another folder within the specified user's mailbox by creating a new copy of the message in the destination folder.

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

        Permanently deletes a message in a user's mailbox and moves it to the Purges folder using the Microsoft Graph API.

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

        Replies to an email message using the Microsoft Graph API by sending a response to the original message based on the provided message ID and user ID.

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

        Sends a reply to all recipients of a specified message using the Microsoft Graph API, creating and sending the email in a single call.

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

        Sends a specified message using the Microsoft Graph API.

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

        Retrieves the count of messages for a specific user, using the provided user ID and optionally applying search and filter parameters.

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

        Tracks changes in messages for a specific user using the Microsoft Graph API, allowing retrieval of newly created, updated, or deleted messages based on optional query parameters such as change type and filtering options.

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
            self.usr_inf_class_override_count,
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
            self.usr_mail_fldr_child_fldr_list_msg_rule,
            self.usr_mail_fldr_child_fldr_create_msg_rule,
            self.usr_mail_fldr_child_fldr_get_msg_rule,
            self.usr_mail_fldr_child_fldr_update_msg_rule,
            self.usr_mail_fldr_child_fldr_delete_msg_rule,
            self.usr_mail_fldr_child_fldr_msg_rule_count,
            self.user_mail_folder_child_folder_list_message,
            self.user_mail_folder_child_folder_create_message,
            self.user_mail_folder_child_folder_get_message,
            self.user_mail_folder_child_folder_update_message,
            self.user_mail_folder_child_folder_delete_message,
            self.usr_mail_fldr_child_fldr_get_msgs_content,
            self.usr_mail_fldr_child_fldr_set_msgs_content,
            self.usr_mail_fldr_child_fldr_delete_msgs_content,
            self.usr_mail_fldr_child_fldr_msg_list_attach,
            self.usr_mail_fldr_child_fldr_msg_create_attach,
            self.usr_mail_fldr_child_fldr_msg_get_attach,
            self.usr_mail_fldr_child_fldr_msg_delete_attach,
            self.usr_mail_fldr_child_fldr_msg_attach_count,
            self.usr_mail_fldr_child_fldr_msg_attach_upload,
            self.usr_mail_fldr_child_fldr_msg_list_ext,
            self.usr_mail_fldr_child_fldr_msg_create_ext,
            self.usr_mail_fldr_child_fldr_msg_get_ext,
            self.usr_mail_fldr_child_fldr_msg_update_ext,
            self.usr_mail_fldr_child_fldr_msg_delete_ext,
            self.usr_mail_fldr_child_fldr_msg_ext_count,
            self.user_mail_folder_child_folder_message_copy,
            self.usr_mail_fldr_child_fldr_msg_create_forward,
            self.usr_mail_fldr_child_fldr_msg_create_reply,
            self.usr_mail_fldr_child_fldr_msg_create_reply_all,
            self.user_mail_folder_child_folder_message_forward,
            self.user_mail_folder_child_folder_message_move,
            self.usr_mail_fldr_child_fldr_msg_perm_delete,
            self.user_mail_folder_child_folder_message_reply,
            self.usr_mail_fldr_child_fldr_msg_reply_all,
            self.user_mail_folder_child_folder_message_send,
            self.usr_mail_fldr_child_fldr_msg_count,
            self.user_mail_folder_child_folder_message_delta,
            self.user_mail_folder_child_folder_copy,
            self.user_mail_folder_child_folder_move,
            self.usr_mail_fldr_child_fldr_perm_delete,
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
            self.usr_mail_fldr_msg_attach_upload,
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
