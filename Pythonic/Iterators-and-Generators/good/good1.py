
""""
`map()` is an in-built function in Python 
""""
def sqrt_it(iter):
  return map(lambda x:x**2, iter)
try:
  from numpy import arange as range
except ImportError:
  pass

seq = range(10)
print(sqrt_it(seq))
for i in sqrt_it(seq):
  print(i)
