from enum import Enum
from logging import Logger
from typing import Optional
import re


class WhirlpoolType(Enum):
    WASHER = ("washer", ["WF", ], re.compile("WF[A-Z]*[0-9]{2,}[A-Z]+[A-Z|0-9]*", re.IGNORECASE))
    DISHWASHER = ("dishwasher", ["WD", ], re.compile("WD[A-Z]*[0-9]{2,}[A-Z]+[A-Z|0-9]*", re.IGNORECASE))

    def __init__(self, device_name: str, prefix: str, pattern: str) -> None:
        self.device_name = device_name
        self.prefix = prefix
        self.pattern = pattern


def get_whirlpool_device_type(model_number: str, logger: Logger) -> Optional[WhirlpoolType]:
    for i in WhirlpoolType:
        for prefix in i.prefix:
            if model_number.startswith(prefix):
                logger.info("Device with model number <{}> is a Whirlpool <{}>.".format(model_number, i.device_name))
                return i.device_name
    logger.error("Supplied model number <{}> is not a registered device".format(model_number))
    return None


def get_whirlpool_model_number(label_text: str, logger: Logger) -> Optional[str]:
    for i in WhirlpoolType:
        for each_word in label_text.split(" "):
            match = i.pattern.match(each_word)
            if match:
                logger.info("Found a Whirlpool model number in label: <{}>".format(match.group()))
                logger.info("Word <{}> matched pattern <{}>".format(match.group(), i.pattern))
                return match.group()
        logger.info("Supplied text does not have any Whirlpool model number.\nText: <{}>".format(label_text))
        return None
