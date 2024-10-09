import math

x1 = int(input("x1: "))
y1 = int(input("y1: "))

x2 = int(input("x2: "))
y2 = int(input("y2: "))

a = abs(x1-x2)
b = abs(y1-y2)

print(2*a+2*b,a*b,sep=" ")
