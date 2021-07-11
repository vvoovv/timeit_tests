import timeit, random

numElements = 100

xy = [ (random.uniform(0., 100.), random.uniform(0., 100.)) for _ in range(numElements) ]

def test1():
    x = [e[0] for e in xy]
    y = [e[1] for e in xy]
    minX = min(x)
    maxX = max(x)
    minY = min(y)
    maxY = max(y)

def test2():
    minX = min(e[0] for e in xy)
    maxX = max(e[0] for e in xy)
    minY = min(e[1] for e in xy)
    maxY = max(e[1] for e in xy)

_x = []
_y = []
def test3():
    _x.clear()
    _y.clear()
    _x.extend(e[0] for e in xy)
    _y.extend(e[1] for e in xy)
    minX = min(_x)
    maxX = max(_x)
    minY = min(_y)
    maxY = max(_y)

print( timeit.timeit("test1()", number=100000, globals=globals()) )
print( timeit.timeit("test2()", number=100000, globals=globals()) )
print( timeit.timeit("test3()", number=100000, globals=globals()) )