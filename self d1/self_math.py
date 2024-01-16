# += / -= / *= / %= / **= is augmented assignment opperators
'''''
x = 3.14
y = 4
z = 5
result = round(x)
result = abs(y)
result = pow(4, 3)
result = max(x,y,z)
result = min(x,y,z)

import math

x= 9.1

#print(math.pi)
#print(math.e)
result = math.sqrt(x) #square root
result = math.ceil(x) # rounded up
result = math.floor(x) #rounded down
print(result)
'''''
#hypotenuse
import math

a = float(input("Enter side A : "))
b = float(input("Enter side B : "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"Side C = {c}")