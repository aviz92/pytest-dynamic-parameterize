from _pytest.config import Config


def my_params(config: Config, some_param: str = None) -> list[tuple]:  # pylint: disable=:W0613
    # Example: generate parameters dynamically, using an optional argument
    if some_param == "special":
        return [
            (10, 20, 30),
            (40, 20, 60),
        ]
    return [
        (1, 2, 3),
        (4, 2, 6),
        (7, 2, 9),
    ]
