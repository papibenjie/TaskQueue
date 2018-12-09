from .base_node import BaseNode

class BaseQueue(object):
    """BaseQueue is the base class of all queues"""

    def __init__(self, root):
        self._root = None
        self.root = root

    def run(self, *args, **kwargs):
        return self.root.run(*args, **kwargs)

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, val):
        if not isinstance(val, BaseNode):
            raise ValueError(" '{0}' root node cannot be set to '{1}'".format(self, val))
        self._root = val

    def print(self):
        self.root.print()

    def __str__(self):
        out = "{0}({1})".format(self.__class__.__name__, self.root)
        return out