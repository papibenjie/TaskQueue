from taskQueue import FuncNode, BaseQueue, queue_from_list

def a(x):
    return x + 10

l = [lambda : [1,2,3,4], lambda x: sum(x), lambda x: x*2]

q = queue_from_list(l)
q.root.insert(FuncNode(a))

q.print()