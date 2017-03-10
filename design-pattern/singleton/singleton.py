# creating singleton pattern in python
"""
The use of singleton pattern is follwed when there is need of object which should be 
created only one's a time.
"""

class Singelton:
      __shart_it = {}# this is the important part continue...
      def __init__(self):
          self.__dict__ = self.__shart_it # try it by replacing with `dict()`
          self.status = "init"
      
x = Singelton()

y = Singelton()

print( x.status, y.status )

y.status = "running"

print( x.status, y.status )

print( id(x.status), id(y.status) )

print( id(x), id(y) )
