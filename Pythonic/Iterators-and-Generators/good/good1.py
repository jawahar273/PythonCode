
""""
`map()` is an in-built function in Python 
""""
def sqrt_it(iter):
  return map(lambda x:x**2, iter)

import numpy as np

seq = np.arange(10)
for i in sqrt_it(seq):
  print(i)
