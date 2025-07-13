def my_params(config, some_param=None) -> list[tuple]:
    # Example: generate parameters dynamically, using an optional argument
    if some_param == "special":
        return [(10, 20, 30)]
    return [
        (1, 2, 3),
        (4, 5, 9),
    ]
