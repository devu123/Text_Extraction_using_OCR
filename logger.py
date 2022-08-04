import logging
from settings import LOG, LOG_LEVEL


logger = logging.getLogger("asurion_device_classifier")
logger.setLevel(logging.INFO)

f = logging.Formatter("%(asctime)s- %(levelname)s - %(name)s - %(module)s:%(lineno)d - %(message)s")

if LOG:
    fh_info = logging.FileHandler(LOG)
else:
    fh_info = logging.StreamHandler()


fh_info.setFormatter(f)
fh_info.setLevel(LOG_LEVEL)
logger.addHandler(fh_info)


def get_logger(name=None):
    if name:
        return logger.getChild(name)
    return logger
