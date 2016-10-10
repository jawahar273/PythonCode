r = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def run():
    for i, j in enumerate(r):
       print(r[i])

       
    
# timeit : 1000 loops, best of 3: 920 µs per loop
# timeit without print: 1000000 loops, best of 3: 1.8 µs per loop
