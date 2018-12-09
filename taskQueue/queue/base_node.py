class BaseNode(object):
    """BaseNode is de base class of all node types"""

    def __init__(self):
        self._child = None

    def run(self, *args, **kwargs):
        return self.child.run(*args, **kwargs)

    def insert(self, node):
        if not isinstance(node, self.__class__):
            raise ValueError("Node '{0}' next node cannot be set to '{1}'".format(self, val))
        child = self.child
        self.child = node
        self.child.child = child

    @property
    def child(self):
        return self._child

    @child.setter
    def child(self, val):
        if not isinstance(val, self.__class__):
            raise ValueError("Node '{0}' next node cannot be set to '{1}'".format(self, val))
        self._child = val

    def print(self):
        print(" -> " + str(self), end="")
        if self.child != None:
            self.child.print()
        else:
            print()

    def __str__(self):
        out = "{0}()".format(self.__class__.__name__)
        return out
