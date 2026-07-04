num = input("Enter your number ")
sum = 0
i= 0
while i < len(num):
    sum = sum + int(num[i])
    i=i+1
print(f"Sum of all the digits of number is {sum}")

