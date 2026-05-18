from custom_python_logger import build_logger

from pytest_dynamic_parameterize import LOGGER_NAME

logger = build_logger(project_name=LOGGER_NAME, log_file=True)
logger.info("Hello world")
logger.warning("Hello world")
logger.error("Hello world")
logger.debug("Hello world")
