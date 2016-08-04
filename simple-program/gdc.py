#Eulesis gcd
def gcd(a,b):
  if a == 0: return b
  return gcd(b%a,a)
print("Enter the gcd value a,b")
a = int(input("a:"))
b = int(input("b:"))

print("value of gcd:",gcd(a,b))
