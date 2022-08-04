from logging import Logger
from typing import Optional

from appliances import brands


def extract_model_number_from_text(label_text: str, logger: Logger) -> Optional[str]:
    # only works for samsung, GE, Electrolux for now
    for name, get_model_number in brands.items():
        mod_num = get_model_number(label_text, logger)
        if mod_num is not None:
            return mod_num
    logger.error("Supplied text does not have any model number.\nText: <{}>".format(label_text))
    return None
