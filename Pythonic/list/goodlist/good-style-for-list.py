# if you are going to access a list without index then it is better 
# to follow below style

show = list('hello-word')
for i in range( len(show) ): # len of the list is calculated 
   print( show[i] ) # slicing of index calculate

for i in show:# the aboue style is overhead and this method can be followed 
   print(i)
   
