from enum import Enum
from typing import Callable

from appliances.ElectroluxType import get_electrolux_device_type
from appliances.SamsungType import get_samsung_device_type


class BrandType(Enum):
    SAMSUNG = ("samsung", get_samsung_device_type)
    ELECTROLUX = ("electrolux", get_electrolux_device_type)

    def __init__(self, brand_name: str, get_device_type: Callable) -> None:
        self.brand_name = brand_name
        self.get_device_type = get_device_type
