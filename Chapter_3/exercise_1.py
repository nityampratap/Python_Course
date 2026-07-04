import random
rand_num = random.randint(1,10)
user_num = int(input("Enter number btw 1 to 10"))
if(user_num == rand_num):
    print("YOU WON")
elif(user_num < rand_num):
    print("ToO LOW")
else:
    print("TOO HIGH")
print(f"WINNING NUMBER IS:{rand_num}")