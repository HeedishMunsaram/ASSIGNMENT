upper = 0
lower = 0
digit = 0
specialcharacter = 0
sentence = input("Please enter your sentence: ")
for var in sentence:
    if var.isalnum():

        if var.isupper():
            upper = upper + 1

        elif var.islower():
            lower = lower + 1

        elif var.isdigit():
            digit = digit + 1

        elif not(var.isalnum()):
            specialcharacter = specialcharacter + 1

print("The number of uppercase alphabet is", upper)
print("The number of lowercase alphabet is", lower)
print("The number of digit is ", digit)
print("The number of special character is ", specialcharacter)

