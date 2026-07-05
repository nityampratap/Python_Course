#def to reverse the item inside list
def rev_item(l):
    a=[]
    for i in l:
        a.append(i[::-1])
    return a
print(rev_item(["erd","abc","fsfgs"]))