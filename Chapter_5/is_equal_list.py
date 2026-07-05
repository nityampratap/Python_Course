# == - we use  == to check if the values of two lists are same or not
# is - we use is to check if the tw2o list share the same memory location or not 

alpha= ["a","b","d","g","j"]
gen=["d","t","s","a"]
beta=["d","b","g","j","a"]
alpha2= ["a","b","d","g","j"]
print(alpha==alpha2)

print (alpha == beta)

print (alpha is gen)

print(alpha is alpha2)