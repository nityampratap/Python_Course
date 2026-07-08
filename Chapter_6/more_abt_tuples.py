#loops in tuples
mix = (1,"two",3,"three")
for i in  mix:
    print(i)

#tuple having one element
one = (1)#it is not a tuple it is a int because tuple always takes its input with comma seperation
print(type(one))
two = (2,)#it is tuple it have comma
print(type(two)) 

#tuple without paranthesis
tup = "age" , "name" , "class"
print(type(tup))

#tuple unpackaing
sups = ("atrain", "homelander" ,"starlight" ,"soldierboy")
sup1,sup2,sup3,sup4 = sups
print(sup1 , sup2 , sup3 , sup4)

#list inside tuple - and we can make changes in that list as it is mutable
tuli = ("ds","pych",1,["wait","stop","hold"])
tuli[3].append("Ruko")
print(tuli)
tuli[3].pop(1)
print(tuli)


#min , max ,  sum
mix1 = (1,3,34,53,2,7,56)
print(min(mix1))
print(max(mix1))
print(sum(mix1))