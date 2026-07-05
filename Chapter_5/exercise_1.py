# taking a list of numbers as input and returning list of sq of those numbers
def sq_list(l):
    sq=[]
    for i in l:
        sq.append(int(i)**2)
    return sq

List= input ("Enter the elements of list by seperating them from comma").split(",")
print(sq_list(List))
