#more ways to add data in list
#insert method -  it add the the data in list at the postion where u want
alpha = ["a","b","c","d"]
alpha.insert(2,"z")
print (alpha)

#to join or concatenate two lists we simply add  them 
num = [1,2,3,4]
mix = alpha + num
print (mix)

#we often use extend to concatenate two list but it change the given list (matlb jis bhi list m ham extend func use krenge vo list extend hojaegi  or new list m convert hojaegi)
alpha.extend(num)
print (alpha)

#append method just add whole list as it is in the list with brackets it doesn't add elements of list
alpha.append(num)
print(alpha)