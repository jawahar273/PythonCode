"""
row = 7
       *
      * *
     *   *
    *     *
   *       *
  *         *
 *           *
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *
row = 6
      *
     * *
    *   *
   *     *
  *       *
 *         *
 *         *
  *       *
   *     *
    *   *
     * *
      *

"""


e = int(input("Enter the number of rows:"))

h = round(e/2)
print("half of e:",e,"is",h)
p = "*"
t = []# list

t.append(list(" "*(e+1))) # the e value will be one which hold the value '*'
t[0][e] = p # indexing start from 0...e 

for i in range(1,e):
   s1 = " "*i
   r = " "*(i-1)
   t.append(list(" "*(e-i)+p+s1+r+p))
i = e-1
#print("e:",e,"i:",i) # debuging
while i >= 1: # for 
   s1 = " "*i
   r = " "*(i-1)
   t.append(list(" "*(e-i)+p+s1+r+p))
   i = i-1

t.append(list(" "*(e+1)))

e1 = len(t)

t[e1-1][e] = p
for k in range(e1):
    for j in range(len(t[k])):# like jagged array
      print(t[k][j],end="")
    print()
