a = -3
h = 0.25



for i in range(325,600,25):
    x = i/100
    print(x)
    print(round(pow(x,2)/(pow((x+a),1/2))+0.5*x,3))
