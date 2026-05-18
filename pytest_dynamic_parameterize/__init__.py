from custom_python_logger import get_logger
from dotenv import load_dotenv

from pytest_dynamic_parameterize.const import NOT_SET_PARAMETERS, LOGGER_NAME

load_dotenv()

__all__ = ["NOT_SET_PARAMETERS"]

logger = get_logger(LOGGER_NAME)
