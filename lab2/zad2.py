import random
import math

def chek(pickUsers,varName):
    
    if(pickUsers == 1):
        while True:
            try:
                znach = float(input(varName))
            except ValueError:
                print("Введите число!")
            else:
                break
        return znach;
    else:
        return(random.randint(1,1000))

print("Выберите режим работы программы:\n",
      "1)Ручной ввод\n",
      "2)Автоматический ввод\n")

while True:
    try:
        pickUsers = int(input())
    except ValueError:
        print("Введите 1 или 2!")
    else:
        if(pickUsers != 1 and pickUsers != 2):
            print("Введите 1 или 2!")
        else: break   


x = chek(pickUsers,'x:')
y = chek(pickUsers,'y:')
z = chek(pickUsers,'z:')

a = round((pow(abs(x-2),1/2)-pow(abs(y),1/2))/(1+pow(x,2)/2+pow(y,2)/4),3)
b = round(x*(math.atan(z)+5),3)
