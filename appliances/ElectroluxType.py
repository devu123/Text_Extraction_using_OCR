import re
from enum import Enum
from logging import Logger
from typing import Optional


# Source: https://www.electrical-forensics.com/MajorAppliances/ElectroluxDateCodes.html
class ElectroluxType(Enum):
    DISHWASHER = ("dishwasher", ["H", ], re.compile("H[A-Z]*[0-9]{2,}[A-Z]+[A-Z|0-9]*", re.IGNORECASE))
    DRIER = ("drier", ["D", "E", ], re.compile("[D|E][A-Z]*[0-9]{2,}[A-Z]+[A-Z|0-9]*", re.IGNORECASE))
    REFRIGERATOR = ("refrigerator", ["A", ], re.compile("A[A-Z]*[0-9]{2,}[A-Z]+[A-Z|0-9]*", re.IGNORECASE))
    WASHER = ("washer", ["C", "E", ], re.compile("[C|E][A-Z]*[0-9]{2,}[A-Z]+[A-Z|0-9]*", re.IGNORECASE))

    def __init__(self, device_name: str, prefix: str, pattern: str) -> None:
        self.device_name = device_name
        self.prefix = prefix
        self.pattern = pattern


def get_electrolux_device_type(model_number: str, logger: Logger) -> Optional[ElectroluxType]:
    for i in ElectroluxType:
        for prefix in i.prefix:
            if model_number.startswith(prefix):
                logger.info("Device with model number <{}> is a Electrolux <{}>.".format(model_number, i.device_name))
                return i.device_name
    logger.error("Supplied model number <{}> is not a registered device".format(model_number))
    return None


def get_electrolux_model_number(label_text: str, logger: Logger) -> Optional[str]:
    for i in ElectroluxType:
        for each_word in label_text.split(" "):
            match = i.pattern.match(each_word)
            if match:
                logger.info("Found a Electrolux model number in label: <{}>".format(match.group()))
                logger.info("Word <{}> matched pattern <{}>".format(match.group(), i.pattern))
                return match.group()
        logger.info("Supplied text does not have any Electrolux model number.\nText: <{}>".format(label_text))
        return None
