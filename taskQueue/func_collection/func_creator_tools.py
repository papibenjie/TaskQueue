def func_namer(name, func):
    if not callable(func):
        raise ValueError("'{0}' must be callable.".format(func))
    if not isinstance(name, str):
        raise ValueError("'{0}' names must be a string.".format(name))
    func.__name__ = name
    return func