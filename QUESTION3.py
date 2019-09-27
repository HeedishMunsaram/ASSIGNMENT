x = input("Enter number: ")
def reversenumber(x):
    reverse = 0
    while True:
        y = str(x)
        if y == y[::-1]:
            break
        else:
            z = int(y[::-1])
            x = z+1
            reverse = reverse + 1
    return x
print("The reverse of number is: ", reversenumber(x))