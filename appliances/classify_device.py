from logging import Logger
from typing import Optional

from appliances.Brands import BrandType
from model_num_extractor.extractor import extract_model_number_from_text


def find_brand(label_text: str, logger: Logger) -> Optional[BrandType]:
    contents = label_text.split(" ")
    for brand in BrandType:
        if any(brand.brand_name.lower() in content.lower() for content in contents):
            logger.info("Found a brand in label: <{}>".format(brand.brand_name))
            return brand
    logger.error("No brand detected in label <{}>".format(label_text))
    return None


def classify_device(label_text: str, logger: Logger) -> Optional[str]:
    model_number = extract_model_number_from_text(label_text, logger)
    brand = find_brand(label_text, logger)
    if model_number is not None:
        device_type = brand.get_device_type(model_number, logger)
        logger.info("Found a device type in label: <{}>".format(device_type))
        return device_type
    logger.error("No device type detected in label <{}>".format(label_text))
    return None
