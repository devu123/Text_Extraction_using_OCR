from enum import Enum
from logging import Logger
from typing import Optional
import re


class MaytagType(Enum):
    GENERIC = ("generic", ["M", ], re.compile("M[A-Z]*[0-9]{2,}[A-Z]+[A-Z|0-9]*", re.IGNORECASE))

    def __init__(self, device_name: str, prefix: str, pattern: str) -> None:
        self.device_name = device_name
        self.prefix = prefix
        self.pattern = pattern


def get_maytag_device_type(model_number: str, logger: Logger) -> Optional[MaytagType]:
    for i in MaytagType:
        for prefix in i.prefix:
            if model_number.startswith(prefix):
                logger.info("Device with model number <{}> is a Maytag <{}>.".format(model_number, i.device_name))
                return i.device_name
    logger.error("Supplied model number <{}> is not a registered device".format(model_number))
    return None


def get_maytag_model_number(label_text: str, logger: Logger) -> Optional[str]:
    for i in MaytagType:
        for each_word in label_text.split(" "):
            match = i.pattern.match(each_word)
            if match:
                logger.info("Found a Maytag model number in label: <{}>".format(match.group()))
                logger.info("Word <{}> matched pattern <{}>".format(match.group(), i.pattern))
                return match.group()
        logger.info("Supplied text does not have any Maytag model number.\nText: <{}>".format(label_text))
        return None
