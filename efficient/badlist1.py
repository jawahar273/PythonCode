r = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(r)
e = []
def run():
  for i in range(n):
     if i % 2 == 0:
        e.append(i)
# timeit 100000 loops, best of 3: 3.42 µs per loop
