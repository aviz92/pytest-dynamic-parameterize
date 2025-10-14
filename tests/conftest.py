from custom_python_logger import build_logger

pytest_plugins = [
    "pytest_dynamic_parameterize.dynamic_parameterize",
]

logger = build_logger(project_name="pytest-dynamic-parameterize", log_file=True)
