def maybe(x, getter = lambda x1: y):  # type: ignore # noqa: F821
    return getter(x) if x is not None else None
