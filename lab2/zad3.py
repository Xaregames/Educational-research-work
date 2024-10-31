import math

def prov(select):
    if (select == 1):
        triangle()
    elif (select == 2):
        restangle()
    elif (select == 3):
        Circle()
    else:
        print("")
        
def restangle():
    a = float(input("Введите первую сторону прямоугольник:\t"))
    b = float(input("Введите вторую сторону прямоугольник:\t"))
    print("Площадь прямоугольника:\t",round(a*b,2))

def Circle():
    r = float(input("Введите радиус круга:\t"))
    r = pow(r,2)*math.pi
    print("Площадь круга:\t",round(r,2))

def triangle():
    a = float(input("Введите первую сторону треугольника:\t"))
    b = float(input("Введите вторую сторону треугольника:\t"))
    с = float(input("Введите третью сторону треугольника:\t"))
    if(a+b > с) and (a+с > b) and (с+b > a):
        p = (a+b+с)/2
        print("Площаль треугольника равна: ",round(math.pow(p*(p-a)*(p-b)*(p-с),1/2),2))
    else:
        print("Такого треугольника нет!")

print('1) Треугольник')
print('2) Прямоугольник')
print('3) Круг')

select = int(input())

prov(select)
