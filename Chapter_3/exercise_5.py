import random
count = 1 
rand_num= random.randint(0,100)
while True:
    num= int (input("Enter number btw 0 to 100: "))
    if num < rand_num:
        print ("Too low")
    elif(num > rand_num):
        print("Too high")
    else:
        break
    count +=1
print(f"you guessed correct in {count} time" )

