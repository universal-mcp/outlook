from typing import Any, List, Optional
from .api_segment_base import APISegmentBase


class PlacesApi(APISegmentBase):

    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def place_update_place(
        self,
        place_id: str,
        id: Optional[str] = None,
        address: Optional[dict[str, dict[str, Any]]] = None,
        displayName: Optional[str] = None,
        geoCoordinates: Optional[dict[str, dict[str, Any]]] = None,
        phone: Optional[str] = None,
    ) -> Any:
        """

        Update place

        Args:
            place_id (string): place-id
            id (string): The unique identifier for an entity. Read-only.
            address (object): address
            displayName (string): The name associated with the place.
            geoCoordinates (object): geoCoordinates
            phone (string): The phone number of the place.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.place
        """
        if place_id is None:
            raise ValueError("Missing required parameter 'place-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "address": address,
            "displayName": displayName,
            "geoCoordinates": geoCoordinates,
            "phone": phone,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/places/{place_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def place_delete_place(self, place_id: str) -> Any:
        """

        Delete entity from places

        Args:
            place_id (string): place-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.place
        """
        if place_id is None:
            raise ValueError("Missing required parameter 'place-id'.")
        url = f"{self.main_app_client.base_url}/places/{place_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def place_get_place_as_room(
        self,
        place_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        List places

        Args:
            place_id (string): place-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Entity result.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.place
        """
        if place_id is None:
            raise ValueError("Missing required parameter 'place-id'.")
        url = f"{self.main_app_client.base_url}/places/{place_id}/microsoft.graph.room"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def place_get_place_as_room_list(
        self,
        place_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get the item of type microsoft.graph.place as microsoft.graph.roomList

        Args:
            place_id (string): place-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Entity result.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.place
        """
        if place_id is None:
            raise ValueError("Missing required parameter 'place-id'.")
        url = f"{self.main_app_client.base_url}/places/{place_id}/microsoft.graph.roomList"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def place_as_room_list_list_room(
        self,
        place_id: str,
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

        Get rooms from places

        Args:
            place_id (string): place-id
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
            places.room
        """
        if place_id is None:
            raise ValueError("Missing required parameter 'place-id'.")
        url = f"{self.main_app_client.base_url}/places/{place_id}/microsoft.graph.roomList/rooms"
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

    def place_as_room_list_create_room(
        self,
        place_id: str,
        id: Optional[str] = None,
        address: Optional[dict[str, dict[str, Any]]] = None,
        displayName: Optional[str] = None,
        geoCoordinates: Optional[dict[str, dict[str, Any]]] = None,
        phone: Optional[str] = None,
        audioDeviceName: Optional[str] = None,
        bookingType: Optional[str] = None,
        building: Optional[str] = None,
        capacity: Optional[float] = None,
        displayDeviceName: Optional[str] = None,
        emailAddress: Optional[str] = None,
        floorLabel: Optional[str] = None,
        floorNumber: Optional[float] = None,
        isWheelChairAccessible: Optional[bool] = None,
        label: Optional[str] = None,
        nickname: Optional[str] = None,
        tags: Optional[List[str]] = None,
        videoDeviceName: Optional[str] = None,
    ) -> Any:
        """

        Create new navigation property to rooms for places

        Args:
            place_id (string): place-id
            id (string): The unique identifier for an entity. Read-only.
            address (object): address
            displayName (string): The name associated with the place.
            geoCoordinates (object): geoCoordinates
            phone (string): The phone number of the place.
            audioDeviceName (string): Specifies the name of the audio device in the room.
            bookingType (string): bookingType
            building (string): Specifies the building name or building number that the room is in.
            capacity (number): Specifies the capacity of the room.
            displayDeviceName (string): Specifies the name of the display device in the room.
            emailAddress (string): Email address of the room.
            floorLabel (string): Specifies a descriptive label for the floor, for example, P.
            floorNumber (number): Specifies the floor number that the room is on.
            isWheelChairAccessible (boolean): Specifies whether the room is wheelchair accessible.
            label (string): Specifies a descriptive label for the room, for example, a number or name.
            nickname (string): Specifies a nickname for the room, for example, 'conf room'.
            tags (array): Specifies other features of the room, for example, details like the type of view or furniture type.
            videoDeviceName (string): Specifies the name of the video device in the room.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.room
        """
        if place_id is None:
            raise ValueError("Missing required parameter 'place-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "address": address,
            "displayName": displayName,
            "geoCoordinates": geoCoordinates,
            "phone": phone,
            "audioDeviceName": audioDeviceName,
            "bookingType": bookingType,
            "building": building,
            "capacity": capacity,
            "displayDeviceName": displayDeviceName,
            "emailAddress": emailAddress,
            "floorLabel": floorLabel,
            "floorNumber": floorNumber,
            "isWheelChairAccessible": isWheelChairAccessible,
            "label": label,
            "nickname": nickname,
            "tags": tags,
            "videoDeviceName": videoDeviceName,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/places/{place_id}/microsoft.graph.roomList/rooms"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def place_as_room_list_get_room(
        self,
        place_id: str,
        room_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get rooms from places

        Args:
            place_id (string): place-id
            room_id (string): room-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.room
        """
        if place_id is None:
            raise ValueError("Missing required parameter 'place-id'.")
        if room_id is None:
            raise ValueError("Missing required parameter 'room-id'.")
        url = f"{self.main_app_client.base_url}/places/{place_id}/microsoft.graph.roomList/rooms/{room_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def place_as_room_list_update_room(
        self,
        place_id: str,
        room_id: str,
        id: Optional[str] = None,
        address: Optional[dict[str, dict[str, Any]]] = None,
        displayName: Optional[str] = None,
        geoCoordinates: Optional[dict[str, dict[str, Any]]] = None,
        phone: Optional[str] = None,
        audioDeviceName: Optional[str] = None,
        bookingType: Optional[str] = None,
        building: Optional[str] = None,
        capacity: Optional[float] = None,
        displayDeviceName: Optional[str] = None,
        emailAddress: Optional[str] = None,
        floorLabel: Optional[str] = None,
        floorNumber: Optional[float] = None,
        isWheelChairAccessible: Optional[bool] = None,
        label: Optional[str] = None,
        nickname: Optional[str] = None,
        tags: Optional[List[str]] = None,
        videoDeviceName: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property rooms in places

        Args:
            place_id (string): place-id
            room_id (string): room-id
            id (string): The unique identifier for an entity. Read-only.
            address (object): address
            displayName (string): The name associated with the place.
            geoCoordinates (object): geoCoordinates
            phone (string): The phone number of the place.
            audioDeviceName (string): Specifies the name of the audio device in the room.
            bookingType (string): bookingType
            building (string): Specifies the building name or building number that the room is in.
            capacity (number): Specifies the capacity of the room.
            displayDeviceName (string): Specifies the name of the display device in the room.
            emailAddress (string): Email address of the room.
            floorLabel (string): Specifies a descriptive label for the floor, for example, P.
            floorNumber (number): Specifies the floor number that the room is on.
            isWheelChairAccessible (boolean): Specifies whether the room is wheelchair accessible.
            label (string): Specifies a descriptive label for the room, for example, a number or name.
            nickname (string): Specifies a nickname for the room, for example, 'conf room'.
            tags (array): Specifies other features of the room, for example, details like the type of view or furniture type.
            videoDeviceName (string): Specifies the name of the video device in the room.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.room
        """
        if place_id is None:
            raise ValueError("Missing required parameter 'place-id'.")
        if room_id is None:
            raise ValueError("Missing required parameter 'room-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "address": address,
            "displayName": displayName,
            "geoCoordinates": geoCoordinates,
            "phone": phone,
            "audioDeviceName": audioDeviceName,
            "bookingType": bookingType,
            "building": building,
            "capacity": capacity,
            "displayDeviceName": displayDeviceName,
            "emailAddress": emailAddress,
            "floorLabel": floorLabel,
            "floorNumber": floorNumber,
            "isWheelChairAccessible": isWheelChairAccessible,
            "label": label,
            "nickname": nickname,
            "tags": tags,
            "videoDeviceName": videoDeviceName,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/places/{place_id}/microsoft.graph.roomList/rooms/{room_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def place_as_room_list_delete_room(self, place_id: str, room_id: str) -> Any:
        """

        Delete navigation property rooms for places

        Args:
            place_id (string): place-id
            room_id (string): room-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.room
        """
        if place_id is None:
            raise ValueError("Missing required parameter 'place-id'.")
        if room_id is None:
            raise ValueError("Missing required parameter 'room-id'.")
        url = f"{self.main_app_client.base_url}/places/{place_id}/microsoft.graph.roomList/rooms/{room_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def place_as_room_list_room_get_count(
        self, place_id: str, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Get the number of the resource

        Args:
            place_id (string): place-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.room
        """
        if place_id is None:
            raise ValueError("Missing required parameter 'place-id'.")
        url = f"{self.main_app_client.base_url}/places/{place_id}/microsoft.graph.roomList/rooms/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def place_get_count(
        self, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Get the number of the resource

        Args:
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.place
        """
        url = f"{self.main_app_client.base_url}/places/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def place_list_place_as_room(
        self,
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

        List places

        Args:
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
            places.place
        """
        url = f"{self.main_app_client.base_url}/places/microsoft.graph.room"
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

    def place_get_count_as_room(
        self, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Get the number of the resource

        Args:
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.place
        """
        url = f"{self.main_app_client.base_url}/places/microsoft.graph.room/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def place_list_place_as_room_list(
        self,
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

        Get the items of type microsoft.graph.roomList in the microsoft.graph.place collection

        Args:
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
            places.place
        """
        url = f"{self.main_app_client.base_url}/places/microsoft.graph.roomList"
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

    def place_get_count_as_room_list(
        self, search: Optional[str] = None, filter: Optional[str] = None
    ) -> Any:
        """

        Get the number of the resource

        Args:
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            places.place
        """
        url = f"{self.main_app_client.base_url}/places/microsoft.graph.roomList/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.place_update_place,
            self.place_delete_place,
            self.place_get_place_as_room,
            self.place_get_place_as_room_list,
            self.place_as_room_list_list_room,
            self.place_as_room_list_create_room,
            self.place_as_room_list_get_room,
            self.place_as_room_list_update_room,
            self.place_as_room_list_delete_room,
            self.place_as_room_list_room_get_count,
            self.place_get_count,
            self.place_list_place_as_room,
            self.place_get_count_as_room,
            self.place_list_place_as_room_list,
            self.place_get_count_as_room_list,
        ]
