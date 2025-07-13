import importlib
import types
from itertools import product

import pytest
from _pytest.config import Parser, Config


def import_from_str(path: str):
    """Import a function from a full dotted path string."""
    module_path, func_name = path.rsplit(".", 1)
    module = importlib.import_module(module_path)
    return getattr(module, func_name)


def resolve_func(func_name: str, metafunc):
    return (
            metafunc.function.__globals__.get(func_name)
            or globals().get(func_name)
    )


def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        "--dynamic-param",
        action="store_true",
        default=False,
        help="Enable dynamic parameterization of tests using a function",
    )


def pytest_configure(config: Config) -> None:
    if not config.getoption("--dynamic-param"):
        return

    config._better_report_enabled = config.getoption("--dynamic-param")


@pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_generate_tests(metafunc):
    if not metafunc.config.getoption("--dynamic-param"):
        yield
        return

    param_func_marks = list(metafunc.definition.iter_markers(name="parametrize_func"))
    if not param_func_marks:
        return

    value_list = []
    parametrize_dict = {}
    for param_func_mark in param_func_marks:
        func_path = param_func_mark.args[0]

        param_func = resolve_func(func_path, metafunc)
        if not isinstance(param_func, types.FunctionType):
            try:
                param_func = import_from_str(func_path)
            except Exception as e:
                raise ValueError(
                    f'Cannot import the function "{func_path}"\n'
                    f'please import the function in your test module or provide a full dotted path. '
                    f'(for example: "module.submodule.function")'
                )

        for mark in metafunc.definition.iter_markers(name="parametrize"):
            parametrize_dict[mark.args[0]] = mark.args[1]

        values = param_func(metafunc.config, *param_func_mark.args[1:], **param_func_mark.kwargs)
        value_list.append(values)

    if value_list:
        combinations = [
            tuple(item for group in combo for item in group)
            for combo in product(*value_list)
        ]
        metafunc.parametrize(
            argnames=[x for x in metafunc.fixturenames if x not in parametrize_dict],
            argvalues=combinations,
            indirect=False,
            # ids=[",".join(f"{n}={v}" for n, v in zip(argnames, row)) for row in values],
        )

    yield