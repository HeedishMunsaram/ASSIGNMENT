a = ["voltaren", "panadol", "meltus", "lecitone", "antibiotics", "aspirin"]
b = print(a)

additem = input("Enter your item: ")
additem = a.append(additem)
print(a)

removeitem = input("Which item do you wish to eject? ")
removeitem = a.remove(removeitem)
print(a)

a.insert(3, "bandage")
print(a)