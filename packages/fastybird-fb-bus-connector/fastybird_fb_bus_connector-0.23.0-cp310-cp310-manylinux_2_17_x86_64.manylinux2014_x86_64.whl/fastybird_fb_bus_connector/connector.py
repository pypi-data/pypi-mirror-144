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
FastyBird BUS connector module
"""

# Python base dependencies
import logging
import re
import uuid
from datetime import datetime
from typing import Dict, Optional, Union

# Library dependencies
from fastybird_devices_module.connectors.connector import IConnector
from fastybird_devices_module.entities.channel import (
    ChannelControlEntity,
    ChannelDynamicPropertyEntity,
    ChannelEntity,
    ChannelPropertyEntity,
    ChannelStaticPropertyEntity,
)
from fastybird_devices_module.entities.connector import ConnectorControlEntity
from fastybird_devices_module.entities.device import (
    DeviceControlEntity,
    DeviceDynamicPropertyEntity,
    DevicePropertyEntity,
)
from fastybird_devices_module.exceptions import RestartConnectorException
from fastybird_devices_module.repositories.device import DevicesRepository
from fastybird_metadata.devices_module import (
    ConnectionState,
    DeviceModel,
    FirmwareManufacturer,
    HardwareManufacturer,
)
from fastybird_metadata.helpers import normalize_value
from fastybird_metadata.types import (
    ButtonPayload,
    ControlAction,
    DataType,
    SwitchPayload,
)
from kink import inject

from fastybird_fb_bus_connector.clients.client import Client
from fastybird_fb_bus_connector.consumers.consumer import Consumer
from fastybird_fb_bus_connector.entities import FbBusDeviceEntity
from fastybird_fb_bus_connector.events.listeners import EventsListener
from fastybird_fb_bus_connector.logger import Logger
from fastybird_fb_bus_connector.registry.model import DevicesRegistry, RegistersRegistry

# Library libs
from fastybird_fb_bus_connector.transporters.transporter import ITransporter
from fastybird_fb_bus_connector.types import (
    ConnectorAction,
    RegisterAttribute,
    RegisterName,
)


@inject(alias=IConnector)
class FbBusConnector(IConnector):  # pylint: disable=too-many-instance-attributes
    """
    FastyBird BUS connector

    @package        FastyBird:FbBusConnector!
    @module         connector

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __stopped: bool = False

    __connector_id: uuid.UUID

    __devices_repository: DevicesRepository

    __packets_to_be_sent: int = 0

    __consumer: Consumer
    __client: Client

    __devices_registry: DevicesRegistry
    __registers_registry: RegistersRegistry

    __transporter: ITransporter

    __events_listener: EventsListener

    __logger: Union[Logger, logging.Logger]

    # -----------------------------------------------------------------------------

    def __init__(  # pylint: disable=too-many-arguments
        self,
        connector_id: uuid.UUID,
        devices_repository: DevicesRepository,
        consumer: Consumer,
        client: Client,
        devices_registry: DevicesRegistry,
        registers_registry: RegistersRegistry,
        transporter: ITransporter,
        events_listener: EventsListener,
        logger: Union[Logger, logging.Logger] = logging.getLogger("dummy"),
    ) -> None:
        self.__connector_id = connector_id

        self.__devices_repository = devices_repository

        self.__client = client
        self.__consumer = consumer

        self.__devices_registry = devices_registry
        self.__registers_registry = registers_registry

        self.__transporter = transporter

        self.__events_listener = events_listener

        self.__logger = logger

    # -----------------------------------------------------------------------------

    @property
    def id(self) -> uuid.UUID:  # pylint: disable=invalid-name
        """Connector identifier"""
        return self.__connector_id

    # -----------------------------------------------------------------------------

    def initialize(self, settings: Optional[Dict] = None) -> None:
        """Set connector to initial state"""
        self.__devices_registry.reset()

        for device in self.__devices_repository.get_all_by_connector(connector_id=self.__connector_id):
            self.initialize_device(device=device)

    # -----------------------------------------------------------------------------

    def initialize_device(self, device: FbBusDeviceEntity) -> None:
        """Initialize device in connector registry"""
        device_record = self.__devices_registry.append(
            device_id=device.id,
            device_enabled=False,
            device_serial_number=device.identifier,
            hardware_manufacturer=device.hardware_manufacturer.value
            if isinstance(device.hardware_manufacturer, HardwareManufacturer)
            else device.hardware_manufacturer,
            hardware_model=device.hardware_model.value
            if isinstance(device.hardware_model, DeviceModel)
            else device.hardware_model,
            hardware_version=device.hardware_version,
            firmware_manufacturer=device.firmware_manufacturer.value
            if isinstance(device.firmware_manufacturer, FirmwareManufacturer)
            else device.firmware_manufacturer,
            firmware_version=device.firmware_version,
        )

        # Channel & channel properties have to be initialized first!
        for channel in device.channels:
            self.initialize_device_channel(device=device, channel=channel)

        # Device properties have to be initialized after channel!
        for device_property in device.properties:
            self.initialize_device_property(device=device, device_property=device_property)

        if device.enabled:
            self.__devices_registry.enable(device=device_record)

    # -----------------------------------------------------------------------------

    def remove_device(self, device_id: uuid.UUID) -> None:
        """Remove device from connector registry"""
        self.__devices_registry.remove(device_id=device_id)

    # -----------------------------------------------------------------------------

    def reset_devices(self) -> None:
        """Reset devices registry to initial state"""
        self.__devices_registry.reset()

    # -----------------------------------------------------------------------------

    def initialize_device_property(self, device: FbBusDeviceEntity, device_property: DevicePropertyEntity) -> None:
        """Initialize device property aka attribute register in connector registry"""

    # -----------------------------------------------------------------------------

    def remove_device_property(self, device: FbBusDeviceEntity, property_id: uuid.UUID) -> None:
        """Remove device property from connector registry"""

    # -----------------------------------------------------------------------------

    def reset_devices_properties(self, device: FbBusDeviceEntity) -> None:
        """Reset devices properties registry to initial state"""

    # -----------------------------------------------------------------------------

    def initialize_device_channel(self, device: FbBusDeviceEntity, channel: ChannelEntity) -> None:
        """Initialize device channel aka registers group in connector registry"""
        register_id: Optional[uuid.UUID] = None
        register_address: Optional[int] = None
        register_data_type: Optional[DataType] = None
        register_queryable: bool = False
        register_settable: bool = False

        for channel_property in channel.properties:
            if (
                channel_property.identifier == RegisterAttribute.ADDRESS.value
                and isinstance(channel_property, ChannelStaticPropertyEntity)
                and isinstance(channel_property.value, int)
            ):
                register_address = channel_property.value

            if channel_property.identifier == RegisterAttribute.VALUE.value and isinstance(
                channel_property, ChannelDynamicPropertyEntity
            ):
                register_id = channel_property.id
                register_data_type = channel_property.data_type
                register_queryable = channel_property.queryable
                register_settable = channel_property.settable

        if register_id is None or register_address is None or register_data_type is None:
            self.__logger.warning(
                "Channel does not have expected properties and can't be mapped to register",
                extra={
                    "device": {
                        "id": channel.device.id.__str__(),
                    },
                    "channel": {
                        "id": channel.device.id.__str__(),
                    },
                },
            )

            return

        match = re.compile("(?P<name>[a-zA-Z_]+)_(?P<address>[0-9]+)")

        parsed_channel_identifier = match.fullmatch(channel.identifier)

        if parsed_channel_identifier is None:
            self.__registers_registry.append_attribute_register(
                device_id=channel.device.id,
                register_id=register_id,
                register_address=register_address,
                register_data_type=register_data_type,
                register_name=channel.identifier,
                register_settable=register_settable,
                register_queryable=register_queryable,
            )

        else:
            if parsed_channel_identifier.group("name") == RegisterName.OUTPUT.value:
                self.__registers_registry.append_output_register(
                    device_id=channel.device.id,
                    register_id=register_id,
                    register_address=register_address,
                    register_data_type=register_data_type,
                )

            elif parsed_channel_identifier.group("name") == RegisterName.INPUT.value:
                self.__registers_registry.append_input_register(
                    device_id=channel.device.id,
                    register_id=register_id,
                    register_address=register_address,
                    register_data_type=register_data_type,
                )

            else:
                self.__logger.warning(
                    "Channel identifier is not as expected. Register couldn't be mapped",
                    extra={
                        "device": {
                            "id": channel.device.id.__str__(),
                        },
                        "channel": {
                            "id": channel.device.id.__str__(),
                        },
                    },
                )

    # -----------------------------------------------------------------------------

    def remove_device_channel(self, device: FbBusDeviceEntity, channel_id: uuid.UUID) -> None:
        """Remove device channel from connector registry"""
        self.__registers_registry.remove(register_id=channel_id)

    # -----------------------------------------------------------------------------

    def reset_devices_channels(self, device: FbBusDeviceEntity) -> None:
        """Reset devices channels registry to initial state"""
        self.__registers_registry.reset(device_id=device.id)

    # -----------------------------------------------------------------------------

    def initialize_device_channel_property(
        self,
        channel: ChannelEntity,
        channel_property: ChannelPropertyEntity,
    ) -> None:
        """Initialize device channel property aka input or output register in connector registry"""

    # -----------------------------------------------------------------------------

    def remove_device_channel_property(self, channel: ChannelEntity, property_id: uuid.UUID) -> None:
        """Remove device channel property from connector registry"""

    # -----------------------------------------------------------------------------

    def reset_devices_channels_properties(self, channel: ChannelEntity) -> None:
        """Reset devices channels properties registry to initial state"""

    # -----------------------------------------------------------------------------

    def start(self) -> None:
        """Start connector services"""
        # When connector is starting...
        self.__events_listener.open()

        for device in self.__devices_registry:
            # ...set device state to unknown
            self.__devices_registry.set_state(device=device, state=ConnectionState.UNKNOWN)

        self.__logger.info("Connector has been started")

        self.__stopped = False

    # -----------------------------------------------------------------------------

    def stop(self) -> None:
        """Close all opened connections & stop connector"""
        # When connector is closing...
        for device in self.__devices_registry:
            # ...set device state to disconnected
            self.__devices_registry.set_state(device=device, state=ConnectionState.DISCONNECTED)

        self.__events_listener.close()

        self.__logger.info("Connector has been stopped")

        self.__stopped = True

    # -----------------------------------------------------------------------------

    def has_unfinished_tasks(self) -> bool:
        """Check if connector has some unfinished task"""
        return not self.__consumer.is_empty()

    # -----------------------------------------------------------------------------

    def handle(self) -> None:
        """Run connector service"""
        if self.__stopped and not self.has_unfinished_tasks():
            self.__logger.warning("Connector is stopped and can't process another requests")

            return

        self.__consumer.handle()

        if self.__stopped:
            return

        # Continue processing devices
        self.__client.handle()

        self.__transporter.handle()

    # -----------------------------------------------------------------------------

    def write_property(self, property_item: Union[DevicePropertyEntity, ChannelPropertyEntity], data: Dict) -> None:
        """Write device or channel property value to device"""
        if self.__stopped:
            self.__logger.warning("Connector is stopped, value can't be written")

            return

        if isinstance(property_item, (DeviceDynamicPropertyEntity, ChannelDynamicPropertyEntity)):
            register_record = self.__registers_registry.get_by_id(register_id=property_item.id)

            if register_record is None:
                return

            if property_item.data_type is not None:
                value_to_write = normalize_value(
                    data_type=property_item.data_type,
                    value=data.get("expected_value", None),
                    value_format=property_item.format,
                )

            else:
                value_to_write = data.get("expected_value", None)

            if (
                isinstance(value_to_write, (str, int, float, bool, datetime, ButtonPayload, SwitchPayload))
                or value_to_write is None
            ):
                if (
                    isinstance(value_to_write, SwitchPayload)
                    and register_record.data_type == DataType.SWITCH
                    and value_to_write == SwitchPayload.TOGGLE
                ):
                    if register_record.actual_value == SwitchPayload.ON:
                        value_to_write = SwitchPayload.OFF

                    else:
                        value_to_write = SwitchPayload.ON

                self.__registers_registry.set_expected_value(register=register_record, value=value_to_write)

                return

    # -----------------------------------------------------------------------------

    def write_control(
        self,
        control_item: Union[ConnectorControlEntity, DeviceControlEntity, ChannelControlEntity],
        data: Optional[Dict],
        action: ControlAction,
    ) -> None:
        """Write connector control action"""
        if isinstance(control_item, ConnectorControlEntity):
            if not ConnectorAction.has_value(control_item.name):
                return

            control_action = ConnectorAction(control_item.name)

            if control_action == ConnectorAction.DISCOVER:
                self.__client.discover()

            if control_action == ConnectorAction.RESTART:
                raise RestartConnectorException("Restarting connector")
