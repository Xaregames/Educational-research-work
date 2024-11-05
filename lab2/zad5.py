
sum = 0

for i in range(1,9):
    for j in range(1,i+1):
        sum += pow(j,2)
        

print("Выражение 1:\t",sum)

sum = 0

for i in range(1,9):
    for j in range(1,2*i+1):
        sum += pow(j,3) + pow(i,2)

        
print("Выражение 2:\t",sum)



sum = 0

for i in range(1,9):
    for j in range(1,i+1):
        for k in range(1,4):
            sum += pow(j,2) + i*k

        
print("Выражение 3:\t",sum)
