# def to take a list of numbers as input and making a list containing lists split into even and odd seperately 
def split_even_odd(l):
    odd=[]
    even=[]
    split=[]
    for i  in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    split.append(even)
    split.append(odd)
    return split
print(split_even_odd([1,2,3,4,5,6,7,655,76,3,4,34,5,34,512]))