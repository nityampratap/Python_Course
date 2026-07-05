#def to take a  list as input and give total number of list inside that ist as output
def list_in_list(l):
    num=0
    for i in l:
        if type(i)== list:
            num +=1
    return num

print(list_in_list([12,[12,33],[3,54],[4,34,234]]))