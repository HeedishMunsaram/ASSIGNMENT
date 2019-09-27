storelist = [ ]
oddlist = [ ]
evenlist = [ ]

print("Code to identify odd & even number from a list")

a = input("Enter number: ")


for x in storelist:
    if (int(x) % 2) == 0:
        b = evenlist.append(x)
    else:
        b = oddlist.append(x)

print("List containing Odd numbers only: ", oddlist)
print("List containing Even numbers only: ", evenlist)











