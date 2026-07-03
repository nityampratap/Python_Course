name , character = input ("Enter your name and any character from a to z seperated by comma").split(",")
print (f"Length of your name is: {len(name)}")
lower_name , lower_char= name.strip().lower() , character.strip().lower()
print(f"{character} is {lower_name.count(lower_char)} times in {name}")
# we use .strip() to remove any accidental whitespace from the user's input.