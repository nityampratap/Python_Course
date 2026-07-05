def greatest(a,b,c):
    if (a>b and a>c):
        return a,"is greater"
    elif (b>a and b>c):
        return b,"is greater"
    return c,"is greater"

n1=int(input("Enter 1st number"))
n2=int(input("Enter 2nd number"))
n3=int(input("Enter 3rd number"))
print(greatest(n1,n2,n3))
