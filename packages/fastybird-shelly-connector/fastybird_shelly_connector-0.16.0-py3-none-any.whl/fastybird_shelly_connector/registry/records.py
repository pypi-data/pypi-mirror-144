#!/usr/bin/python3

#     Copyright 2021. FastyBird s.r.o.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

"""
Shelly connector registry module records
"""

# Python base dependencies
import uuid
from datetime import datetime
from typing import List, Optional, Set, Tuple, Union

# Library dependencies
from fastybird_metadata.devices_module import ConnectionState
from fastybird_metadata.helpers import normalize_value
from fastybird_metadata.types import ButtonPayload, DataType, SwitchPayload

# Library libs
from fastybird_shelly_connector.types import (
    ClientType,
    DeviceAttribute,
    DeviceCommandType,
    DeviceDescriptionSource,
    SensorType,
    SensorUnit,
)


class DeviceRecord:  # pylint: disable=too-many-public-methods,too-many-instance-attributes
    """
    Shelly device record

    @package        FastyBird:ShellyConnector!
    @module         registry/records

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __id: uuid.UUID  # Generated by connector

    __identifier: str  # Provided by Shelly device
    __type: Optional[str] = None  # Provided by Shelly device
    __mac_address: Optional[str] = None  # Provided by Shelly device
    __firmware_version: Optional[str] = None  # Provided by Shelly device

    __enabled: bool = False

    __name: Optional[str] = None

    __username: Optional[str] = None
    __password: Optional[str] = None

    __description_source: Set[DeviceDescriptionSource] = set()

    __last_communication_timestamp: Optional[float] = None

    # -----------------------------------------------------------------------------

    def __init__(  # pylint: disable=too-many-arguments
        self,
        device_id: uuid.UUID,
        device_identifier: str,
        device_type: Optional[str] = None,
        device_mac_address: Optional[str] = None,
        device_firmware_version: Optional[str] = None,
        device_enabled: bool = False,
        device_name: Optional[str] = None,
    ) -> None:
        self.__id = device_id
        self.__identifier = device_identifier
        self.__type = device_type
        self.__mac_address = device_mac_address
        self.__firmware_version = device_firmware_version
        self.__name = device_name
        self.__enabled = device_enabled

        self.__description_source = set()

        self.__last_communication_timestamp = None

    # -----------------------------------------------------------------------------

    @property
    def id(self) -> uuid.UUID:  # pylint: disable=invalid-name
        """Device unique identifier"""
        return self.__id

    # -----------------------------------------------------------------------------

    @property
    def identifier(self) -> str:
        """Device unique shelly identifier"""
        return self.__identifier

    # -----------------------------------------------------------------------------

    @property
    def type(self) -> Optional[str]:
        """Device hardware model"""
        return self.__type

    # -----------------------------------------------------------------------------

    @property
    def mac_address(self) -> Optional[str]:
        """Device hardware mac address"""
        return self.__mac_address

    # -----------------------------------------------------------------------------

    @property
    def firmware_version(self) -> Optional[str]:
        """Device firmware version"""
        return self.__firmware_version

    # -----------------------------------------------------------------------------

    @property
    def initialized(self) -> bool:
        """Is device fully initialized?"""
        return DeviceDescriptionSource.MANUAL in self.__description_source or (
            (
                DeviceDescriptionSource.COAP_DESCRIPTION in self.__description_source
                or DeviceDescriptionSource.HTTP_DESCRIPTION in self.__description_source
            )
            and DeviceDescriptionSource.HTTP_SHELLY in self.__description_source
            and DeviceDescriptionSource.HTTP_STATUS in self.__description_source
        )

    # -----------------------------------------------------------------------------

    @property
    def description_source(self) -> Set[DeviceDescriptionSource]:
        """Device description sources"""
        return self.__description_source

    # -----------------------------------------------------------------------------

    def add_description_source(self, description_source: DeviceDescriptionSource) -> None:
        """Add new description source"""
        self.__description_source.add(description_source)

    # -----------------------------------------------------------------------------

    @property
    def name(self) -> Optional[str]:
        """Device unique name"""
        return self.__name

    # -----------------------------------------------------------------------------

    @name.setter
    def name(self, name: Optional[str] = None) -> None:
        """Set device unique name"""
        self.__name = name

    # -----------------------------------------------------------------------------

    @property
    def username(self) -> Optional[str]:
        """HTTP authentication username"""
        return self.__username

    # -----------------------------------------------------------------------------

    @username.setter
    def username(self, username: Optional[str] = None) -> None:
        """Set HTTP authentication username"""
        self.__username = username

    # -----------------------------------------------------------------------------

    @property
    def password(self) -> Optional[str]:
        """HTTP authentication password"""
        return self.__password

    # -----------------------------------------------------------------------------

    @password.setter
    def password(self, password: Optional[str] = None) -> None:
        """Set HTTP authentication password"""
        self.__password = password

    # -----------------------------------------------------------------------------

    @property
    def enabled(self) -> bool:
        """Is device enabled?"""
        return self.__enabled

    # -----------------------------------------------------------------------------

    @property
    def last_communication_timestamp(self) -> Optional[float]:
        """Last device communication timestamp"""
        return self.__last_communication_timestamp

    # -----------------------------------------------------------------------------

    @last_communication_timestamp.setter
    def last_communication_timestamp(self, last_communication_timestamp: Optional[float]) -> None:
        """Set last device communication timestamp"""
        self.__last_communication_timestamp = last_communication_timestamp

    # -----------------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DeviceRecord):
            return False

        return (
            self.id == other.id
            and self.identifier == other.identifier
            and self.type == other.type
            and self.mac_address == other.mac_address
            and self.firmware_version == other.firmware_version
            and self.username == other.username
            and self.password == other.password
        )

    # -----------------------------------------------------------------------------

    def __hash__(self) -> int:
        return self.__id.__hash__()


class BlockRecord:  # pylint: disable=too-many-public-methods,too-many-instance-attributes
    """
    Device block record

    @package        FastyBird:ShellyConnector!
    @module         registry/records

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __device_id: uuid.UUID

    __id: uuid.UUID  # Generated by connector

    __identifier: int  # Provided by Shelly device
    __description: str  # Provided by Shelly device

    # -----------------------------------------------------------------------------

    def __init__(  # pylint: disable=too-many-arguments
        self,
        device_id: uuid.UUID,
        block_id: uuid.UUID,
        block_identifier: int,
        block_description: str,
    ) -> None:
        self.__device_id = device_id

        self.__id = block_id
        self.__identifier = block_identifier
        self.__description = block_description

    # -----------------------------------------------------------------------------

    @property
    def device_id(self) -> uuid.UUID:
        """Block device unique identifier"""
        return self.__device_id

    # -----------------------------------------------------------------------------

    @property
    def id(self) -> uuid.UUID:  # pylint: disable=invalid-name
        """Block unique identifier"""
        return self.__id

    # -----------------------------------------------------------------------------

    @property
    def identifier(self) -> int:
        """Block unique shelly identifier"""
        return self.__identifier

    # -----------------------------------------------------------------------------

    @property
    def description(self) -> str:
        """Block description"""
        return self.__description

    # -----------------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BlockRecord):
            return False

        return (
            self.device_id == other.device_id
            and self.id == other.id
            and self.identifier == other.identifier
            and self.description == other.description
        )

    # -----------------------------------------------------------------------------

    def __hash__(self) -> int:
        return self.__id.__hash__()


class SensorRecord:  # pylint: disable=too-many-public-methods,too-many-instance-attributes
    """
    Block sensor & state record

    @package        FastyBird:ShellyConnector!
    @module         registry/records

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __block_id: uuid.UUID

    __id: uuid.UUID  # Generated by connector

    __identifier: int  # Provided by Shelly device
    __type: SensorType  # Provided by Shelly device
    __description: str  # Provided by Shelly device
    __unit: Optional[SensorUnit]  # Provided by Shelly device
    __value_format: Union[
        Tuple[Optional[int], Optional[int]],
        Tuple[Optional[float], Optional[float]],
        List[Union[str, Tuple[str, Optional[str], Optional[str]]]],
        None,
    ] = None  # Provided by Shelly device
    __value_invalid: Union[str, int, float, bool, None]  # Provided by Shelly device
    __data_type: DataType  # Generated by connector

    __queryable: bool = False
    __settable: bool = False

    __actual_value: Union[str, int, float, bool, datetime, ButtonPayload, SwitchPayload, None] = None
    __expected_value: Union[str, int, float, bool, datetime, ButtonPayload, SwitchPayload, None] = None
    __expected_pending: Optional[float] = None

    # -----------------------------------------------------------------------------

    def __init__(  # pylint: disable=too-many-arguments
        self,
        block_id: uuid.UUID,
        sensor_id: uuid.UUID,
        sensor_identifier: int,
        sensor_type: SensorType,
        sensor_description: str,
        sensor_data_type: DataType,
        sensor_unit: Optional[SensorUnit] = None,
        sensor_value_format: Union[
            Tuple[Optional[int], Optional[int]],
            Tuple[Optional[float], Optional[float]],
            List[Union[str, Tuple[str, Optional[str], Optional[str]]]],
            None,
        ] = None,
        sensor_value_invalid: Union[str, int, float, bool, None] = None,
        sensor_queryable: bool = False,
        sensor_settable: bool = False,
    ) -> None:
        self.__block_id = block_id

        self.__id = sensor_id
        self.__identifier = sensor_identifier
        self.__type = sensor_type
        self.__description = sensor_description
        self.__unit = sensor_unit
        self.__value_format = sensor_value_format
        self.__value_invalid = sensor_value_invalid

        self.__data_type = sensor_data_type

        self.__queryable = sensor_queryable
        self.__settable = sensor_settable

    # -----------------------------------------------------------------------------

    @property
    def block_id(self) -> uuid.UUID:
        """Sensor&State block unique identifier"""
        return self.__block_id

    # -----------------------------------------------------------------------------

    @property
    def id(self) -> uuid.UUID:  # pylint: disable=invalid-name
        """Sensor&State unique identifier"""
        return self.__id

    # -----------------------------------------------------------------------------

    @property
    def identifier(self) -> int:
        """Sensor&State unique shelly identifier"""
        return self.__identifier

    # -----------------------------------------------------------------------------

    @property
    def type(self) -> SensorType:
        """Sensor&State type"""
        return self.__type

    # -----------------------------------------------------------------------------

    @property
    def description(self) -> str:
        """Sensor&State description"""
        return self.__description

    # -----------------------------------------------------------------------------

    @property
    def unit(self) -> Optional[SensorUnit]:
        """Sensor&State optional unit"""
        return self.__unit

    # -----------------------------------------------------------------------------

    @property
    def data_type(self) -> DataType:
        """Sensor&State optional value data type"""
        return self.__data_type

    # -----------------------------------------------------------------------------

    @property
    def format(
        self,
    ) -> Union[
        Tuple[Optional[int], Optional[int]],
        Tuple[Optional[float], Optional[float]],
        List[Union[str, Tuple[str, Optional[str], Optional[str]]]],
        None,
    ]:
        """Sensor&State optional value format"""
        return self.__value_format

    # -----------------------------------------------------------------------------

    @property
    def invalid(self) -> Union[str, int, float, bool, None]:
        """Sensor&State optional value invalid"""
        return self.__value_invalid

    # -----------------------------------------------------------------------------

    @property
    def queryable(self) -> bool:
        """Is sensor&state queryable?"""
        return self.__queryable

    # -----------------------------------------------------------------------------

    @property
    def settable(self) -> bool:
        """Is sensor&state settable?"""
        return self.__settable

    # -----------------------------------------------------------------------------

    @property
    def actual_value(self) -> Union[str, int, float, bool, datetime, ButtonPayload, SwitchPayload, None]:
        """Sensor&State actual value"""
        return normalize_value(data_type=self.data_type, value=self.__actual_value, value_format=self.format)

    # -----------------------------------------------------------------------------

    @actual_value.setter
    def actual_value(self, value: Union[str, int, float, bool, datetime, ButtonPayload, SwitchPayload, None]) -> None:
        """Set sensor&state actual value"""
        self.__actual_value = value

        if self.actual_value == self.expected_value:
            self.expected_value = None
            self.expected_pending = None

        if self.expected_value is None:
            self.expected_pending = None

    # -----------------------------------------------------------------------------

    @property
    def expected_value(self) -> Union[str, int, float, bool, datetime, ButtonPayload, SwitchPayload, None]:
        """Sensor&State expected value"""
        return normalize_value(data_type=self.data_type, value=self.__expected_value, value_format=self.format)

    # -----------------------------------------------------------------------------

    @expected_value.setter
    def expected_value(self, value: Union[str, int, float, bool, datetime, ButtonPayload, SwitchPayload, None]) -> None:
        """Set sensor&state expected value"""
        self.__expected_value = value
        self.expected_pending = None

    # -----------------------------------------------------------------------------

    @property
    def expected_pending(self) -> Optional[float]:
        """Sensor&State expected value pending status"""
        return self.__expected_pending

    # -----------------------------------------------------------------------------

    @expected_pending.setter
    def expected_pending(self, timestamp: Optional[float]) -> None:
        """Set sensor&state expected value transmit timestamp"""
        self.__expected_pending = timestamp

    # -----------------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SensorRecord):
            return False

        return (
            self.block_id == other.block_id
            and self.id == other.id
            and self.identifier == other.identifier
            and self.type == other.type
            and self.description == other.description
            and self.unit == other.unit
            and self.data_type == other.data_type
            and self.format == other.format
            and self.invalid == other.invalid
            and self.settable == other.settable
            and self.queryable == other.queryable
        )

    # -----------------------------------------------------------------------------

    def __hash__(self) -> int:
        return self.__id.__hash__()


class AttributeRecord:  # pylint: disable=too-many-public-methods,too-many-instance-attributes
    """
    Device attribute record

    @package        FastyBird:ShellyConnector!
    @module         registry/records

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __device_id: uuid.UUID

    __id: uuid.UUID
    __type: DeviceAttribute
    __value: Union[int, float, str, bool, datetime, ButtonPayload, SwitchPayload, None] = None

    # -----------------------------------------------------------------------------

    def __init__(  # pylint: disable=too-many-arguments
        self,
        device_id: uuid.UUID,
        attribute_id: uuid.UUID,
        attribute_type: DeviceAttribute,
        attribute_value: Union[int, float, str, bool, datetime, ButtonPayload, SwitchPayload, None] = None,
    ) -> None:
        self.__device_id = device_id

        self.__id = attribute_id
        self.__type = attribute_type
        self.__value = attribute_value

    # -----------------------------------------------------------------------------

    @property
    def device_id(self) -> uuid.UUID:
        """Device unique identifier"""
        return self.__device_id

    # -----------------------------------------------------------------------------

    @property
    def id(self) -> uuid.UUID:  # pylint: disable=invalid-name
        """Attribute unique identifier"""
        return self.__id

    # -----------------------------------------------------------------------------

    @property
    def type(self) -> DeviceAttribute:
        """Attribute type"""
        return self.__type

    # -----------------------------------------------------------------------------

    @property
    def value(self) -> Union[int, float, str, bool, datetime, ButtonPayload, SwitchPayload, None]:
        """Attribute value"""
        return self.__value

    # -----------------------------------------------------------------------------

    @value.setter
    def value(self, value: Union[int, float, str, bool, datetime, ButtonPayload, SwitchPayload, None]) -> None:
        """Set attribute value"""
        self.__value = value

    # -----------------------------------------------------------------------------

    @property
    def actual_value(self) -> Union[int, float, str, bool, datetime, ButtonPayload, SwitchPayload, None]:
        """Attribute value"""
        return self.__value

    # -----------------------------------------------------------------------------

    @actual_value.setter
    def actual_value(self, value: Union[int, float, str, bool, datetime, ButtonPayload, SwitchPayload, None]) -> None:
        """Set attribute value"""
        self.__value = value

    # -----------------------------------------------------------------------------

    @property
    def data_type(self) -> Optional[DataType]:
        """Attribute data type"""
        if self.type == DeviceAttribute.STATE:
            return DataType.ENUM

        if self.type == DeviceAttribute.AUTH_ENABLED:
            return DataType.BOOLEAN

        return DataType.STRING

    # -----------------------------------------------------------------------------

    @property
    def format(
        self,
    ) -> Union[List[str], Tuple[Optional[int], Optional[int]], Tuple[Optional[float], Optional[float]], None]:
        """Attribute format"""
        if self.type == DeviceAttribute.STATE:
            return [
                ConnectionState.CONNECTED.value,
                ConnectionState.DISCONNECTED.value,
                ConnectionState.INIT.value,
                ConnectionState.LOST.value,
                ConnectionState.UNKNOWN.value,
            ]

        return None

    # -----------------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AttributeRecord):
            return False

        return (
            self.device_id == other.device_id
            and self.id == other.id
            and self.type == other.type
            and self.data_type == other.data_type
            and self.format == other.format
            and self.actual_value == other.actual_value
        )

    # -----------------------------------------------------------------------------

    def __hash__(self) -> int:
        return self.__id.__hash__()


class CommandRecord:  # pylint: disable=too-many-public-methods,too-many-instance-attributes
    """
    Device processed command record

    @package        FastyBird:ShellyConnector!
    @module         registry/records

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __device_id: uuid.UUID
    __client_type: ClientType
    __command_type: DeviceCommandType
    __command_timestamp: float = 0.0
    __command_status: bool = False

    def __init__(  # pylint: disable=too-many-arguments
        self,
        device_id: uuid.UUID,
        client_type: ClientType,
        command_type: DeviceCommandType,
        command_timestamp: float,
        command_status: bool,
    ) -> None:
        self.__device_id = device_id

        self.__client_type = client_type

        self.__command_type = command_type
        self.__command_status = command_status
        self.__command_timestamp = command_timestamp

    # -----------------------------------------------------------------------------

    @property
    def device_id(self) -> uuid.UUID:
        """Device unique identifier"""
        return self.__device_id

    # -----------------------------------------------------------------------------

    @property
    def client_type(self) -> ClientType:
        """Sent command via client type"""
        return self.__client_type

    # -----------------------------------------------------------------------------

    @property
    def command_type(self) -> DeviceCommandType:
        """Sent command type"""
        return self.__command_type

    # -----------------------------------------------------------------------------

    @property
    def command_timestamp(self) -> float:
        """Sent command timestamp"""
        return self.__command_timestamp

    # -----------------------------------------------------------------------------

    @property
    def command_status(self) -> bool:
        """Sent command status"""
        return self.__command_status

    # -----------------------------------------------------------------------------

    def __str__(self) -> str:
        return f"{self.client_type.value}_{self.command_type.value}_{self.device_id.__str__()}"

    # -----------------------------------------------------------------------------

    def __hash__(self) -> int:
        return hash((self.command_type, self.command_type, self.device_id))
