from taskQueue import FuncNode, BaseQueue, queue_from_list

def event(msg):
    return int(input(msg))


def sum_list(l, b):
    return sum(l)

def pow2(n):
    return n ** 2

def mul10(n):
    return n * 10


l = [event, pow2, mul10]

q = queue_from_list(l)

q.print()

print( q.run("Nb: ") )