'''
     *
    ***
   *****
  *******
  for r = 5
'''

r = int(input())
k = 0
for i in range(0,r):
  print(" "*((r)-i),((i)*"*")+("*"*(i-1)))
