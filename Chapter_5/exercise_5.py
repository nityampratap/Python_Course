#def to take two list as input and return a list of common elemnts in them
def common(j,k):
    cm=[]
    for i in j:
        for r in k:
            if i==r:
                cm.append(i)
    return cm
print(common([1,2,3,4],[3,4,1,5,52,1,2]))