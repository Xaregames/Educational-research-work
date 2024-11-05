import math

p = int(input())
x = 7
y = math.exp(math.log(x*(p+1))/p)

def schet(eps,y,x,p):
    n = 0
    
    while True:
        n = n + 1
        yn = 1/p*((p-1)*y + x/pow(y,p-1))
        
        if(abs(yn - y)<= eps):
            print("{0}\t{1}\t{2}".format(eps,yn,n))
            break
        else:
            y = yn

    


for i in range(-2,-7,-1):
    eps = pow(10, i)
    n = 0
    schet(eps,y,x,p)
    


    
print(math.exp(math.log(x*(p+1))/p))
print(pow(x,1/p))
