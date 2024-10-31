n = int(input("Введите n: "))
n1 = 1;
n2 = 1;
i=2

while(i <= n):
    n2 = n1 + n2
    i = i + 1
    if(i== n):
        print('n-ый элемент ряда равен: ',n2)
        break
    n1 = n1 + n2
    i = i + 1
    if(i== n):
        print('n-ый элемент ряда равен: ',n1)
        break

if (n==1)or(n==2):
    print('Значение n-го элемента ряда фибаначи равно: 1 ')
elif (n<0):
    print('n должно быть больше 0!')
