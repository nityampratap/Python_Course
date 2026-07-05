#methods to delete data from the list
alpha = ["a","b","c","d","e","f","g","h","f"]
#1st pop- it takes the index value as input which we want to delete
alpha.pop(2)
print(alpha)
#if no argument is passed it default delete last element

#2nd del method it also  take index value
del alpha[:3]
print(alpha)

#3rd remove method it takes the elemnt as  input which we want to delete
alpha.remove("f")
print(alpha)
#if there are two same elements it default delete first one
