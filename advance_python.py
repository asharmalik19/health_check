#reduce function in python. it takes a function and a list (iterable), applies the function accumulatively on the whole list and returns one result.

from functools import reduce 

def sum(a, b):
  return a+b
  
li = [1, 2, 3, 4]
res = reduce(sum, li)
print(res)