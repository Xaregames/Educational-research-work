import math

X = int(input("X: "))
A = int(input("A: "))
Y = int(input("Y: "))
B = int(input("B: "))

A = A/X
B = B/Y

print(round(A,5),round(B,5),round(A/B,5),sep="\n")
