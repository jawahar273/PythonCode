"""
this game is just a huch..
Name1:romeo
Name2:juliet
flames are
"""

n1 = input("Name1:") #"romeo"
n2 = input("Name2:")#"juliet"
n1 = "".join(n1.split())
n2 = "".join(n2.split())
from collections import Counter as count

s1 = count(n1)
s2 = count(n2)
su = 0
t = s1 - s2
#print(t)# debugging
su = sum(t.values())
#print(su)# debugging
t = ( s2 - s1 )
#print(t)# debugging
su = sum(t.values()) + su
#print(su)# debugging
su-=1# to cal in the be of position in string indexing startes from 0..len()
q = 'flames'
l = len(q)
#print(q)# debugging
#print("------"*5,"working","------"*5)
while l>1:
   e = su%l
   q = "".join(q.split(q[e]))
   q = q[e:]+q.strip(q[e:])  
   #print("l:",l,"q:",q)# debugging
   #print(q)
   l-=1
#print("------"*5,"------"*5)
q1 = {'f':'friends','l':'love','a':'attraction','m':'marriage','e':'enemies','s':'sister'}
print("flames are:")
print(q1[q])



