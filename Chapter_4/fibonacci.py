#0 1 1 2 3 5 8 13 21 34
def  fibo(a):
    x=0
    y=1
    if a==1:
        print(x)
    elif a==2:
        print(x,y)
    else:
        print (x,y,end=(" "))
        for i in range (a-2):
            b= x+y
            x=y
            y=b
            print(y,end=(" "))
fibo(10)