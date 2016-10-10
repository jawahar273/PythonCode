r = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def run():
  for  i in range(len(r)):
    print(i)

# timeit with print: 1000 loops, best of 3: 2.81 ms per loop
# timeit without print: 1000000 loops, best of 3: 1.82 µs per loop
