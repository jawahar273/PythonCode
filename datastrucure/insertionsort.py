us = [89, 45, 68, 90, 29, 34, 17]
def sort(a): # insertion sort...
   n = len(a)
   for i in range(1, n):
   	   insetsort(a, i, a[i])

def insetsort(b ,i ,value):
   	 i -= 1
   	 i1 = 0
   	 i2 = 0
   	 while i >= 0 and b[i] > value:

   	    b[i + 1] = b[i]
   	    i1 = b[i] # <- comment this 
   	    #* len(str(pointer[i+1]))
   	    i -= 1

   	    b[i + 1] = value
   	    i2 = value # <- comment this 

   	 print(b)
   	 print("1:",i1,"\n2:",i2,end="\n\n") # <- comment this ; comment all this if you don't understands

sort(us)
print(us)# insertion sort...
