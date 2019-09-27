num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

num3 = min(num1, num2)

while(True):
    if(num3 % num1 == 0 and num3 % num2 == 0):
        print("LCM of 2 number is: ", num3)
        break
    num3 = num3 + 1