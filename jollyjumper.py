

""""
jolly jummper sequances:
 if the absolute values of the differences between the successive elements take on all possible values from 1 through n-1
 Input: 1 4 2 3
Output: True
the absolute differences are 3, 2, and 1.

Input: 1 4 2 -1 6  
Output: False
The absolute differences are 3, 2, 3, 7.

references :
http://users.csc.calpoly.edu/~jdalbey/301/Labs/JollyJumpers.html
see geekforgeek.com also if this like didnot work.
"""



t = [1, 4, 2, -1, 6 ] # not Jolly jumper sequance
m = max(t)-1
print("the max value in the list (max(x)-1):",m)
jj = "Jolly jumper sequance"
def y():
  for i in range(1,len(t)):
    d = abs(t[i]-t[i-1])
    print("abs differnt for t[",i,"] and t[",i-1,"]:",i,d)
    if(d > m):
         print("not a ",end="")
         break
    
  
y()
print(jj,length of the list:,len(t))
