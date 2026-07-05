def  greater(a,b):
    if a>b:
        return a
    return b

def greatest(a,b,c):
    high = greater(a,b)
    return greater(high,c)

print(greatest(100,23,44))