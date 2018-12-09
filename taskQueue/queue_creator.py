from .func_node import FuncNode
from .base_node import BaseNode
from .base_queue import BaseQueue

def queue_from_list(funcs):
    _validate_func_list(funcs)
    if len(funcs) == 0:
        return BaseQueue(BaseNode())
    elif len(funcs) == 1:
        return BaseQueue(FuncNode(funcs[0]))
    else:
        root = FuncNode(funcs[0])
        node = root
        for i in range(1, len(funcs)):
            node.child = FuncNode(funcs[i])
            node = node.child
        return BaseQueue(root)



def _validate_func_list(funcs):
    if not isinstance(funcs, list):
        raise ValueError("A list of functions is needed to create a queue, '{0}' was passed.".format(funcs))
    for f in funcs:
        if not callable(f):
            raise ValueError("All elements in list '{0}' must be callable, '{1}' is not.".format(funcs, f))


