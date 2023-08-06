"""

"""


import logging
from logging.config import dictConfig
import os

import yaml


CONF_PATH = os.path.join("trajcalc", "logger", "config.yaml")

with open(CONF_PATH, "r", encoding="utf-8") as file:
    dictConfig(
        yaml.safe_load(file.read())
    )

logger = logging.getLogger(__name__)

logger.debug("Configured logger (%s)", CONF_PATH)
