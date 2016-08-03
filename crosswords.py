

"""
P     m
 r   a
  o r
   g
  o r
 r   a
P     m
this is only for odd value strings only.
even value will be something different...check that out

"""
t = []

p = input()#'Program'
def inc(a):
    r  = a%2
    return a+r

l = len(p)
l2= inc(l//2)
r = l-1

print(p,"\n",r,"\nlen:",l,"\nhalf len",l2)

for i in range(l):
    t.append(list(" "*l))	

print(len(t[0]))

tr = 0

for i in range(l2):
 
     t[i][tr] = p[i]
     t[i][r] =  p[r]
     tr+=1
     r-=1


for i in range(l2,l):
     t[i][tr] = p[i]
     t[i][r] =  p[r] 
     r-=1
     tr+=1
     
for i in range(l):
  for j in range(l):
   print(t[i][j],end="")
  print()

