#function take a list as input and return it in reverse order
def reverse_list(l):
    rev = []
    for i in range(len(l)-1,-1,-1):
        rev.append(l[i])
    return rev
print(reverse_list([1,2,3,"word",4,5,"s"]))
