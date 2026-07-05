# genrating list with range function
num = list(range(1,11))
print(num)
num2=[1,3,4,6,2,54,2,3,32,5,2,3,34,42,1,]
# pop method also give popped value
dele = num.pop()
print(dele)

# index method
print(num2.index(2))
# first value say about finding element which element u want to find 2nd value say about after which index value you want to start searching for 1st value and 3rd value is the range i.e btw 2nd and 3rd index value the searching for that element occur 

# list to a function
def negative_list(a):
    d=[]
    for i in a:
        d.append(-i)
    return d
print(negative_list([1,2,3]))

