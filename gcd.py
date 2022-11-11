def gcd(a: int, b: int) -> int:
    while a and b:
        a, b = b, a % b
    return a or b
  
  
  
  
def gcd(a,b):
    if (b == 0):
         return a
    return gcd(b, a%b)
print(gcd(5,5))
