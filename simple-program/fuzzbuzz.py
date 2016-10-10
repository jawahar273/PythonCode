"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print 'Fizz' instead of the number and for the multiples of five print 'Buzz'. 
For numbers which are multiples of both three and five print 'FizzBuzz'.
"""
def t():
 for i in range(1, 101):
   j = i % 3
   k = i % 5
   print(i,end="")
   if j == 0:
     print('\nFizz',end="")
   if k == 0:
   	 print('Buzz')

   print()

t()
