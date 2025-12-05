import pytest
from custom_python_logger import get_logger

# from tests.parameterize_functions.my_params import my_params

logger = get_logger(__name__)


@pytest.mark.parametrize_func("tests.parameterize_functions.my_params.my_params")
def test_add(a: int, b: int, expected: int) -> None:
    logger.info(f"{a} + {b} = {expected}")
    assert a + b == expected


@pytest.mark.parametrize_func("tests.parameterize_functions.my_params.my_params", some_param="special")
def test_add_special(a: int, b: int, expected: int) -> None:
    logger.info(f"{a} + {b} = {expected}")
    assert a + b == expected


@pytest.mark.parametrize_func("tests.parameterize_functions.my_params.my_params", some_param="special")
@pytest.mark.parametrize_func("tests.parameterize_functions.my_params.my_params")
def test_add_multi(a1: int, b1: int, expected1: int, a2: int, b2: int, expected2: int) -> None:
    logger.info(f"{a1} + {b1} = {expected1}")
    logger.info(f"{a2} + {b2} = {expected2}")
    assert a1 + b1 == expected1
    assert a2 + b2 == expected2
