from homeassistant.components.sensor import SensorEntity
from homeassistant.components.sensor import SensorEntityDescription

from ..common.entity_controller import EntityController
from .modbus_entity_mixin import ModbusEntityMixin


class ConnectionStatusSensor(ModbusEntityMixin, SensorEntity):
    def __init__(
        self,
        controller: EntityController,
    ) -> None:
        self.entity_description = SensorEntityDescription(
            key="connection_status",
            name="Connection Status",
        )
        self._controller = controller

    @property
    def native_value(self) -> str | None:
        if self._controller.current_connection_error is None:
            self._attr_icon = "mdi:check"
            return "Connected"

        self._attr_icon = "mdi:alert-outline"
        return self._controller.current_connection_error

    @property
    def available(self) -> bool:
        return True

    @property
    def addresses(self) -> list[int]:
        return []
