"""
check if the integer is a prime number
"""


from math import sqrt

a = int(input("pls input a integer: "))
end = int(sqrt(a))
is_prime = True
for i in range(2,end+1):
   if a%i == 0:
      is_prime = False
if is_prime and a != 1:
   print("%d is a prime number" % a)
else:
   print("%d is not a prime number" % a)

   

"""
get max common divisor and least common multipler
"""


a = int(input("pls input integer a: "))
b = int(input("pls input integer b: "))
x = min(a, b)
while (a % x != 0 or b % x != 0 and x > 1):
   x -= 1
y = a * b / x
print("%d and %d 's max common divisor and least common multipler are %d and %d" % (a, b, x, y))



"""
print triangle
"""


r = int(input("pls input triangle row number:"))
for i in range(1, r+1):
   for j in range(i):
      print("*", end = "")
   print()

for i in range(1, r+1):
   for j in range(r-i):
      print(" ", end = "")
   for k in range(i):
      print("*", end = "")
   print()    

for i in range(1, r+1):
   for j in range(r-i):
      print(" ", end = "")
   for k in range(2*(i-1)+1):
      print("*", end = "")
   print() 
