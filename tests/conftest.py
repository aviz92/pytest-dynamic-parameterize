from custom_python_logger import build_logger

logger = build_logger(project_name="pytest-dynamic-parameterize", log_file=True)
logger.info("Hello world")
logger.warning("Hello world")
logger.error("Hello world")
logger.debug("Hello world")
