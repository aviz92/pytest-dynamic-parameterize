import pytest
from tests.parameterize_functions.parametrize_functions.my_params import my_params

@pytest.mark.parametrize_func("tests.parameterize_functions.parametrize_functions.my_params.my_params")
def test_add(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize_func("tests.parameterize_functions.parametrize_functions.my_params.my_params", some_param="special")
def test_add_special(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize_func("tests.parameterize_functions.parametrize_functions.my_params.my_params", some_param="special")
@pytest.mark.parametrize_func("tests.parameterize_functions.parametrize_functions.my_params.my_params")
def test_add_multi(a1, b1, expected1, a2, b2, expected2):
    assert a1 + b1 == expected1
    assert a2 + b2 == expected2
