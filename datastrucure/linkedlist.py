class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None
    #self.pre = None


class slist:
 
   def __init__(self):
     self.t = Node()
     self.root = Node('0')
     self.t.next  = self.root
     for i in list('123456789'):
       self.temp = Node(i)
       self.root.next = self.temp
       self.root = self.temp
     self.display()

   def search(self, sea):
      p = self.t
      while p.next != None:
        if sea == p.data:
        	return 'found'
        p = p.next

      return 'not found'

   def remove(self, sea):
   
      cur = self.t
      pre = None
      while cur.next != None and cur.data != sea:
         pre = cur
         cur = cur.next

      if cur is not None :
          if cur is self.t :
            self.t = cur.next
          else :
            pre.next = cur.next 

   def display(self):
   
      p = self.t
      while p.next != None:
        print(p.data)
        p = p.next

e= slist();
e.remove('6')
print(e.search('6'))
e.display()
