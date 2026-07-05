#ordered collection of item ----> list
#you can store anything in list like str , int , float etc
numbers = [1 ,2 ,3 ,4]
print(numbers)

words = ["Word1","Word2","Word3"]
print(words)

mixed = [1,2,3,"Four",3.16,None]
print(mixed)

print(words[2])

print(numbers[:3])#3-1 tak jaegi value from 0

mixed[2]="Three"

print (mixed)

mixed[:2]=["two"]
print (mixed)