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
Devices module connectors connector worker module
"""

# Python base dependencies
import pkgutil
import re
import time
import types
import uuid
from abc import ABC, abstractmethod
from importlib import util as import_util
from typing import Dict, Optional, Union

from fastybird_metadata.devices_module import ConnectionState, ConnectorPropertyName

# Library libs
from fastybird_metadata.routing import RoutingKey
from fastybird_metadata.types import ControlAction, DataType
from inflection import dasherize
from kink import di
from sqlalchemy.orm import close_all_sessions

# Library dependencies
from fastybird_devices_module.connectors.queue import (
    ConnectorQueue,
    ConsumeControlActionMessageQueueItem,
    ConsumeEntityMessageQueueItem,
    ConsumePropertyActionMessageQueueItem,
)
from fastybird_devices_module.entities.channel import (
    ChannelControlEntity,
    ChannelEntity,
    ChannelPropertyEntity,
)
from fastybird_devices_module.entities.connector import (
    ConnectorControlEntity,
    ConnectorStaticPropertyEntity,
)
from fastybird_devices_module.entities.device import (
    DeviceControlEntity,
    DeviceEntity,
    DevicePropertyEntity,
)
from fastybird_devices_module.exceptions import (
    RestartConnectorException,
    TerminateConnectorException,
)
from fastybird_devices_module.logger import Logger
from fastybird_devices_module.managers.connector import ConnectorPropertiesManager
from fastybird_devices_module.repositories.channel import (
    ChannelControlsRepository,
    ChannelPropertiesRepository,
    ChannelsRepository,
)
from fastybird_devices_module.repositories.connector import (
    ConnectorControlsRepository,
    ConnectorPropertiesRepository,
    ConnectorsRepository,
)
from fastybird_devices_module.repositories.device import (
    DeviceControlsRepository,
    DevicePropertiesRepository,
    DevicesRepository,
)


class IConnector(ABC):
    """
    Connector interface

    @package        FastyBird:DevicesModule!
    @module         connectors/connector

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    # -----------------------------------------------------------------------------

    @property
    @abstractmethod
    def id(self) -> uuid.UUID:  # pylint: disable=invalid-name
        """Connector identifier"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def initialize(self, settings: Optional[Dict] = None) -> None:
        """Set connector to initial state"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def initialize_device(self, device: DeviceEntity) -> None:
        """Initialize device in connector"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def remove_device(self, device_id: uuid.UUID) -> None:
        """Remove device from connector"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def reset_devices(self) -> None:
        """Reset devices to initial state"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def initialize_device_property(self, device: DeviceEntity, device_property: DevicePropertyEntity) -> None:
        """Initialize device property in connector"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def remove_device_property(self, device: DeviceEntity, property_id: uuid.UUID) -> None:
        """Remove device from connector"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def reset_devices_properties(self, device: DeviceEntity) -> None:
        """Reset devices properties to initial state"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def initialize_device_channel(self, device: DeviceEntity, channel: ChannelEntity) -> None:
        """Initialize device channel in connector"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def remove_device_channel(self, device: DeviceEntity, channel_id: uuid.UUID) -> None:
        """Remove device channel from connector"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def reset_devices_channels(self, device: DeviceEntity) -> None:
        """Reset devices channels to initial state"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def initialize_device_channel_property(
        self,
        channel: ChannelEntity,
        channel_property: ChannelPropertyEntity,
    ) -> None:
        """Initialize device channel property in connector"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def remove_device_channel_property(self, channel: ChannelEntity, property_id: uuid.UUID) -> None:
        """Remove device channel property from connector"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def reset_devices_channels_properties(self, channel: ChannelEntity) -> None:
        """Reset devices channels properties to initial state"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def start(self) -> None:
        """Start connector service"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def stop(self) -> None:
        """Stop connector service"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def handle(self) -> None:
        """Process connector actions"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def has_unfinished_tasks(self) -> bool:
        """Check if connector has some unfinished tasks"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def write_property(self, property_item: Union[DevicePropertyEntity, ChannelPropertyEntity], data: Dict) -> None:
        """Write device or channel property value to device"""

    # -----------------------------------------------------------------------------

    @abstractmethod
    def write_control(
        self,
        control_item: Union[ConnectorControlEntity, DeviceControlEntity, ChannelControlEntity],
        data: Optional[Dict],
        action: ControlAction,
    ) -> None:
        """Write connector control action"""


class Connector:  # pylint: disable=too-many-instance-attributes
    """
    Connector container

    @package        FastyBird:DevicesModule!
    @module         connectors/connector

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __stopped: bool = False

    __queue: ConnectorQueue

    __connector: Optional[IConnector] = None

    __devices_repository: DevicesRepository
    __devices_properties_repository: DevicePropertiesRepository
    __devices_control_repository: DeviceControlsRepository

    __channels_repository: ChannelsRepository
    __channels_properties_repository: ChannelPropertiesRepository
    __channels_control_repository: ChannelControlsRepository

    __connectors_repository: ConnectorsRepository
    __connectors_properties_repository: ConnectorPropertiesRepository
    __connectors_properties_manager: ConnectorPropertiesManager
    __connectors_control_repository: ConnectorControlsRepository

    __logger: Logger

    __SHUTDOWN_WAITING_DELAY: float = 3.0

    # -----------------------------------------------------------------------------

    def __init__(  # pylint: disable=too-many-arguments
        self,
        queue: ConnectorQueue,
        devices_repository: DevicesRepository,
        devices_properties_repository: DevicePropertiesRepository,
        devices_control_repository: DeviceControlsRepository,
        channels_repository: ChannelsRepository,
        channels_properties_repository: ChannelPropertiesRepository,
        channels_control_repository: ChannelControlsRepository,
        connectors_repository: ConnectorsRepository,
        connectors_properties_repository: ConnectorPropertiesRepository,
        connectors_properties_manager: ConnectorPropertiesManager,
        connectors_control_repository: ConnectorControlsRepository,
        logger: Logger,
    ) -> None:
        self.__queue = queue

        self.__devices_repository = devices_repository
        self.__devices_properties_repository = devices_properties_repository
        self.__devices_control_repository = devices_control_repository

        self.__channels_repository = channels_repository
        self.__channels_properties_repository = channels_properties_repository
        self.__connectors_control_repository = connectors_control_repository

        self.__connectors_repository = connectors_repository
        self.__connectors_properties_repository = connectors_properties_repository
        self.__connectors_properties_manager = connectors_properties_manager
        self.__channels_control_repository = channels_control_repository

        self.__logger = logger

    # -----------------------------------------------------------------------------

    def start(self) -> None:
        """Start connector service"""
        self.__stopped = False

        try:
            if self.__connector is not None:
                self.__set_state(state=ConnectionState.RUNNING)

                self.__connector.start()

        except Exception as ex:  # pylint: disable=broad-except
            self.__logger.error(
                "Connector couldn't be started. An unexpected error occurred",
                extra={
                    "exception": {
                        "message": str(ex),
                        "code": type(ex).__name__,
                    },
                },
            )

            raise TerminateConnectorException("Connector couldn't be started. An unexpected error occurred") from ex

    # -----------------------------------------------------------------------------

    def stop(self) -> None:
        """Stop connector service"""
        self.__stopped = True

        self.__logger.info("Stopping...")

        try:
            # Send terminate command to...

            # ...connector
            if self.__connector is not None:
                self.__connector.stop()

                now = time.time()

                waiting_for_closing = True

                # Wait until thread is fully terminated
                while waiting_for_closing and time.time() - now < self.__SHUTDOWN_WAITING_DELAY:
                    if self.__connector.has_unfinished_tasks():
                        self.__connector.handle()
                    else:
                        waiting_for_closing = False

                self.__set_state(state=ConnectionState.STOPPED)

        except Exception as ex:  # pylint: disable=broad-except
            self.__logger.error(
                "Connector couldn't be stopped. An unexpected error occurred",
                extra={
                    "exception": {
                        "message": str(ex),
                        "code": type(ex).__name__,
                    },
                },
            )

            raise TerminateConnectorException("Connector couldn't be stopped. An unexpected error occurred") from ex

    # -----------------------------------------------------------------------------

    def handle(self) -> None:
        """Process connector actions"""
        # All records have to be processed before thread is closed
        if self.__stopped:
            return

        try:
            if self.__connector is not None:
                self.__connector.handle()

        except Exception as ex:  # pylint: disable=broad-except
            self.__logger.exception(ex)
            self.__logger.error(
                "An unexpected error occurred during connector handling process",
                extra={
                    "exception": {
                        "message": str(ex),
                        "code": type(ex).__name__,
                    },
                },
            )

            raise TerminateConnectorException("An unexpected error occurred during connector handling process") from ex

        queue_item = self.__queue.get()

        if queue_item is not None:
            try:
                if isinstance(queue_item, ConsumePropertyActionMessageQueueItem):
                    self.__write_property_command(item=queue_item)

                if isinstance(queue_item, ConsumeControlActionMessageQueueItem):
                    self.__write_control_command(item=queue_item)

                if isinstance(queue_item, ConsumeEntityMessageQueueItem):
                    self.__handle_entity_event(item=queue_item)

            except Exception as ex:  # pylint: disable=broad-except
                self.__logger.exception(ex)
                self.__logger.error(
                    "An unexpected error occurred during processing queue item",
                    extra={
                        "exception": {
                            "message": str(ex),
                            "code": type(ex).__name__,
                        },
                    },
                )

                raise TerminateConnectorException("An unexpected error occurred during processing queue item") from ex

    # -----------------------------------------------------------------------------

    def load(self, connector_id: uuid.UUID) -> None:
        """Try to load connector"""
        try:
            connectors = self.__import_connectors()

            connector = self.__connectors_repository.get_by_id(connector_id=connector_id)

            if connector is None:
                raise AttributeError(f"Connector {connector_id} was not found in database")

            if dasherize(connector.type) not in connectors:
                raise AttributeError(f"Connector {connector.type} couldn't be loaded")

            module = connectors[dasherize(connector.type)]

            # Add loaded connector to container to be accessible & autowired
            di["connector"] = connector

            self.__connector = getattr(module, "create_connector")(connector=connector, logger=self.__logger)

            if not isinstance(self.__connector, IConnector):
                raise AttributeError(f"Instance of connector {connector.type} couldn't be created")

            self.__connector.initialize(settings=connector.params)

        except Exception as ex:  # pylint: disable=broad-except
            print(ex)
            raise Exception("Connector could not be loaded") from ex

    # -----------------------------------------------------------------------------

    @staticmethod
    def __import_connectors() -> Dict[str, types.ModuleType]:
        connectors: Dict[str, types.ModuleType] = {}

        for module in pkgutil.iter_modules():
            match = re.compile("fastybird_(?P<name>[a-zA-Z_]+)_connector")
            parsed_module_name = match.fullmatch(module.name)

            if parsed_module_name is not None:
                module_spec = import_util.find_spec(name=module.name)

                if module_spec is not None:
                    loaded_module = import_util.module_from_spec(module_spec)
                    module_spec.loader.exec_module(loaded_module)  # type: ignore[union-attr]

                    if hasattr(loaded_module, "create_connector"):
                        connectors[parsed_module_name.group("name")] = loaded_module

        return connectors

    # -----------------------------------------------------------------------------

    def __write_property_command(  # pylint: disable=too-many-return-statements
        self,
        item: ConsumePropertyActionMessageQueueItem,
    ) -> None:
        if self.__connector is None:
            return

        if item.routing_key == RoutingKey.DEVICE_PROPERTY_ACTION:
            try:
                device_property = self.__devices_properties_repository.get_by_id(
                    property_id=uuid.UUID(item.data.get("property"), version=4),
                )

            except ValueError:
                return

            if device_property is None:
                return

            if device_property.parent_id is not None:
                device_property = self.__devices_properties_repository.get_by_id(
                    property_id=uuid.UUID(bytes=device_property.parent_id, version=4),
                )

            if device_property is None:
                return

            self.__connector.write_property(device_property, item.data)

        if item.routing_key == RoutingKey.CHANNEL_PROPERTY_ACTION:
            try:
                channel_property = self.__channels_properties_repository.get_by_id(
                    property_id=uuid.UUID(item.data.get("property"), version=4),
                )

            except ValueError:
                return

            if channel_property is None:
                return

            if channel_property.parent_id is not None:
                channel_property = self.__channels_properties_repository.get_by_id(
                    property_id=uuid.UUID(bytes=channel_property.parent_id, version=4),
                )

            if channel_property is None:
                return

            self.__connector.write_property(channel_property, item.data)

    # -----------------------------------------------------------------------------

    def __write_control_command(  # pylint: disable=too-many-return-statements
        self,
        item: ConsumeControlActionMessageQueueItem,
    ) -> None:
        if self.__connector is None:
            return

        if item.routing_key == RoutingKey.DEVICE_ACTION and ControlAction.has_value(str(item.data.get("name"))):
            try:
                connector_control = self.__connectors_control_repository.get_by_name(
                    connector_id=uuid.UUID(item.data.get("connector"), version=4),
                    control_name=str(item.data.get("name")),
                )

            except ValueError:
                return

            if connector_control is None:
                return

            self.__connector.write_control(
                control_item=connector_control,
                data=item.data,
                action=ControlAction(item.data.get("name")),
            )

        if item.routing_key == RoutingKey.CHANNEL_ACTION and ControlAction.has_value(str(item.data.get("name"))):
            try:
                device_control = self.__devices_control_repository.get_by_name(
                    device_id=uuid.UUID(item.data.get("device"), version=4), control_name=str(item.data.get("name"))
                )

            except ValueError:
                return

            if device_control is None:
                return

            self.__connector.write_control(
                control_item=device_control,
                data=item.data,
                action=ControlAction(item.data.get("name")),
            )

        if item.routing_key == RoutingKey.CONNECTOR_ACTION and ControlAction.has_value(str(item.data.get("name"))):
            try:
                channel_control = self.__channels_control_repository.get_by_name(
                    channel_id=uuid.UUID(item.data.get("channel"), version=4), control_name=str(item.data.get("name"))
                )

            except ValueError:
                return

            if channel_control is None:
                return

            self.__connector.write_control(
                control_item=channel_control,
                data=item.data,
                action=ControlAction(item.data.get("name")),
            )

    # -----------------------------------------------------------------------------

    def __handle_entity_event(  # pylint: disable=too-many-branches,too-many-return-statements,too-many-statements
        self,
        item: ConsumeEntityMessageQueueItem,
    ) -> None:
        if self.__connector is None:
            return

        if item.routing_key == RoutingKey.CONNECTOR_ENTITY_UPDATED:
            close_all_sessions()

            try:
                connector_entity = self.__connectors_repository.get_by_id(
                    connector_id=uuid.UUID(item.data.get("id"), version=4),
                )

                if connector_entity is None or not connector_entity.id.__eq__(di["connector"].id):
                    return

            except ValueError:
                return

            if connector_entity is None:
                self.__logger.warning("Connector was not found in database")

                return

            raise RestartConnectorException(
                "Connector was updated in database, terminating connector service in favor of restarting service"
            )

        if item.routing_key == RoutingKey.CONNECTOR_ENTITY_DELETED:
            close_all_sessions()

            try:
                if not di["connector"].id.__eq__(uuid.UUID(item.data.get("id"), version=4)):
                    return

                raise TerminateConnectorException("Connector was removed from database, terminating connector service")

            except ValueError:
                return

        if item.routing_key in (RoutingKey.DEVICE_ENTITY_CREATED, RoutingKey.DEVICE_ENTITY_UPDATED):
            close_all_sessions()

            try:
                device_entity = self.__devices_repository.get_by_id(
                    device_id=uuid.UUID(item.data.get("id"), version=4),
                )

            except ValueError:
                return

            if device_entity is None:
                self.__logger.warning("Device was not found in database")

                return

            self.__connector.initialize_device(device=device_entity)

        if item.routing_key == RoutingKey.DEVICE_ENTITY_DELETED:
            close_all_sessions()

            try:
                self.__connector.remove_device(uuid.UUID(item.data.get("id"), version=4))

            except ValueError:
                return

        if item.routing_key in (RoutingKey.DEVICE_PROPERTY_ENTITY_CREATED, RoutingKey.DEVICE_PROPERTY_ENTITY_UPDATED):
            close_all_sessions()

            try:
                device_entity = self.__devices_repository.get_by_id(
                    device_id=uuid.UUID(item.data.get("device"), version=4),
                )

            except ValueError:
                return

            if device_entity is None:
                return

            try:
                device_property_entity = self.__devices_properties_repository.get_by_id(
                    property_id=uuid.UUID(item.data.get("id"), version=4),
                )

            except ValueError:
                return

            if device_property_entity is None:
                self.__logger.warning("Device property was not found in database")

                return

            self.__connector.initialize_device_property(device=device_entity, device_property=device_property_entity)

        if item.routing_key == RoutingKey.DEVICE_PROPERTY_ENTITY_DELETED:
            close_all_sessions()

            try:
                device_entity = self.__devices_repository.get_by_id(
                    device_id=uuid.UUID(item.data.get("device"), version=4),
                )

            except ValueError:
                return

            if device_entity is None:
                return

            try:
                self.__connector.remove_device_property(
                    device=device_entity,
                    property_id=uuid.UUID(item.data.get("id"), version=4),
                )

            except ValueError:
                return

        if item.routing_key in (RoutingKey.CHANNEL_ENTITY_CREATED, RoutingKey.CHANNEL_ENTITY_UPDATED):
            close_all_sessions()

            try:
                channel_entity = self.__channels_repository.get_by_id(
                    channel_id=uuid.UUID(item.data.get("id"), version=4),
                )

            except ValueError:
                return

            if channel_entity is None:
                self.__logger.warning("Channel was not found in database")

                return

            try:
                device_entity = self.__devices_repository.get_by_id(
                    device_id=uuid.UUID(item.data.get("device"), version=4),
                )

            except ValueError:
                return

            if device_entity is None:
                self.__logger.warning("Device was not found in database")

                return

            self.__connector.initialize_device_channel(device=device_entity, channel=channel_entity)

        if item.routing_key == RoutingKey.CHANNEL_ENTITY_DELETED:
            close_all_sessions()

            try:
                device_entity = self.__devices_repository.get_by_id(
                    device_id=uuid.UUID(item.data.get("device"), version=4),
                )

            except ValueError:
                return

            if device_entity is None:
                return

            try:
                self.__connector.remove_device_channel(
                    device=device_entity,
                    channel_id=uuid.UUID(item.data.get("id"), version=4),
                )

            except ValueError:
                return

        if item.routing_key in (
            RoutingKey.CHANNEL_PROPERTY_ENTITY_CREATED,
            RoutingKey.CHANNEL_PROPERTY_ENTITY_UPDATED,
        ):
            close_all_sessions()

            try:
                channel_property_entity = self.__channels_properties_repository.get_by_id(
                    property_id=uuid.UUID(item.data.get("id"), version=4),
                )

            except ValueError:
                return

            if channel_property_entity is None:
                self.__logger.warning("Channel property was not found in database")

                return

            try:
                channel_entity = self.__channels_repository.get_by_id(
                    channel_id=uuid.UUID(item.data.get("channel"), version=4),
                )

            except ValueError:
                return

            if channel_entity is None:
                return

            self.__connector.initialize_device_channel_property(
                channel=channel_entity, channel_property=channel_property_entity
            )

        if item.routing_key == RoutingKey.CHANNEL_PROPERTY_ENTITY_DELETED:
            close_all_sessions()

            try:
                channel_entity = self.__channels_repository.get_by_id(
                    channel_id=uuid.UUID(item.data.get("channel"), version=4),
                )

            except ValueError:
                return

            if channel_entity is None:
                return

            try:
                self.__connector.remove_device_channel_property(
                    channel=channel_entity,
                    property_id=uuid.UUID(item.data.get("id"), version=4),
                )

            except ValueError:
                return

    # -----------------------------------------------------------------------------

    def __set_state(self, state: ConnectionState) -> None:
        if self.__connector is not None:
            state_property = self.__connectors_properties_repository.get_by_identifier(
                connector_id=self.__connector.id,
                property_identifier=ConnectorPropertyName.STATE.value,
            )

            if state_property is None:
                property_data = {
                    "connector_id": self.__connector.id,
                    "identifier": ConnectorPropertyName.STATE.value,
                    "data_type": DataType.ENUM,
                    "unit": None,
                    "format": [
                        ConnectionState.RUNNING.value,
                        ConnectionState.STOPPED.value,
                        ConnectionState.UNKNOWN.value,
                        ConnectionState.SLEEPING.value,
                        ConnectionState.ALERT.value,
                    ],
                    "settable": False,
                    "queryable": False,
                    "value": state.value,
                }

                self.__connectors_properties_manager.create(
                    data=property_data,
                    property_type=ConnectorStaticPropertyEntity,
                )

            else:
                property_data = {
                    "value": state.value,
                }

                self.__connectors_properties_manager.update(
                    data=property_data,
                    connector_property=state_property,
                )
