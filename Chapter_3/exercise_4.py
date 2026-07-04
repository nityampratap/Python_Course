name = input("Enter your number: ")
i = 0
str=""
while i<len(name):
    if name[i] not in str:
        print(f"{name[i]} : {name.count(name[i])}")
   
    str = str+ name[i]
    i=i+1
    