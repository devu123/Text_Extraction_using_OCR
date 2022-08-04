from enum import Enum
from logging import Logger
from typing import Optional
import re


class BoschType(Enum):
    # source: https://en.tab-tv.com/?p=13575
    WASHER = ("washer", ["W", ], re.compile("W(?=.*\d)(?=.*[A-Z])[A-Z\d]{8,}", re.IGNORECASE))
    # source: https://whoatwherewhy.com/what-do-bosch-dishwasher-model-numbers-mean/
    FRIDGE = ("fridge", ["B", ], re.compile("B(?=.*\d)(?=.*[A-Z])[A-Z\d]{8,}", re.IGNORECASE))
    MICROWAVE = ("microwave", ["H", ], re.compile("H(?=.*\d)(?=.*[A-Z])[A-Z\d]{8,}", re.IGNORECASE))
    DISHWASHER = ("dishwasher", ["S", ], re.compile("S(?=.*\d)(?=.*[A-Z])[A-Z\d]{8,}", re.IGNORECASE))

    def __init__(self, device_name: str, prefix: str, pattern: str) -> None:
        self.device_name = device_name
        self.prefix = prefix
        self.pattern = pattern


def get_bosch_device_type(model_number: str, logger: Logger) -> Optional[BoschType]:
    for i in BoschType:
        for prefix in i.prefix:
            if model_number.startswith(prefix):
                logger.info("Device with model number <{}> is a Bosch <{}>.".format(model_number, i.device_name))
                return i.device_name
    logger.error("Supplied model number <{}> is not a registered device".format(model_number))
    return None


def get_bosch_model_number(label_text: str, logger: Logger) -> Optional[str]:
    for i in BoschType:
        for each_word in label_text.split(" "):
            match = i.pattern.match(each_word)
            if match:
                logger.info("Found a Bosch model number in label: <{}>".format(match.group()))
                logger.info("Word <{}> matched pattern <{}>".format(match.group(), i.pattern))
                return match.group()
        logger.info("Supplied text does not have any Bosch model number.\nText: <{}>".format(label_text))
        return None