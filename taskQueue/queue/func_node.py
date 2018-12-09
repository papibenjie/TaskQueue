from .base_node import BaseNode

class FuncNode(BaseNode):
    """Class to make func node."""

    def __init__(self, func):
        super().__init__()
        self._func = None
        self.func = func

    def run(self, *args, **kwargs):
        out = self.func(*args, **kwargs)
        if self.child == None:
            return out
        return self.child.run(out)

    @property
    def func(self):
        return self._func

    @func.setter
    def func(self, val):
        if not callable(val):
            raise ValueError("trigger of node '{0}' cannot be set to '{1}'.".format(self, val))
        self._func = val

    def __str__(self):
        out = "{0}(f={1}({2}))".format(self.__class__.__name__, self.func.__name__, ", ".join(self.func.__code__.co_varnames))
        return out