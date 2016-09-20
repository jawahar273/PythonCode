def turns(n, low, high):# gussing algorithum
   turn = 0
   while (high - low)>=2:
      turn +=1
      m = (low + high)//2
      if m == n:
        return turn
      elif m < n:
        low =  m + 1
      else:
        high = m -1
   return turn + 1

print(turns(9,0,10))
