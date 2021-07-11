import timeit

print( timeit.timeit("[i for i in range(100)]", number=100000, globals=globals()) )
print( timeit.timeit("tuple(i for i in range(100))", number=100000, globals=globals()) )
print( timeit.timeit("list(i for i in range(100))", number=100000, globals=globals()) )