alpha = ["a","f","c","d","e","f","g","e","r","t","e"]
#count- it count the no of times element placed in list
print(alpha.count("e"))

#sort- it sort the original list in ascending order 
# alpha.sort()
# print(alpha)

#sorted function - it does not change the original list only sort the list on which function applied 
print(sorted(alpha))
print(alpha)

#reverse - it print the original list in reverse order 
alpha.reverse()
print(alpha)

#clear- it  clear  the elements of the list and make it empty
alpha.clear()
print(alpha)

#copy - it make a duplicate copy of the list 
gen = alpha.copy()
print (gen)