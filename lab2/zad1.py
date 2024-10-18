x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

k = round((y1-y2)/(x1-x2),3)
b = round(y1 - k*x1,3)

if(b > 0):
    print("y = {0}x+{1}".format(k,b))
elif (b == 0):
    print("y = {0}x".format(k))
else:
    print("y = {0}x{1}".format(k,b))
