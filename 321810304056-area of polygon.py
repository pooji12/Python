


import math
n = float(input("number of sides: "))
s= float(input("length of a side: "))
p = n * (s** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is: ",p)