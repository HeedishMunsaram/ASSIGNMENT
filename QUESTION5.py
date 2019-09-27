num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

while num1 % num2 != 0:
    num3 = num1 % num2
    num1 = num2
    num2 = num3

print("The HCF of numbers is ", num2)
