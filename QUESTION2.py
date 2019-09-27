w = input("Please enter 4 list of 4 values :")
m = w.split()
x = input("Please enter 4 list of 4 values :")
n = w.split()
y = input("Please enter 4 list of 4 values :")
o = w.split()
z = input("Please enter 4 list of 4 values :")
p = w.split()

def add1(m):
    for num1 in m:
        global var1
        var1 = int(var1) + int(num1)
    return var1

def add2(n):
    for num2 in n:
        global var2
        var2 = int(var2) + int(num2)
    return var2

def add3(o):
    for num3 in o:
        global var3
        var3 = int(var3) + int(num3)
    return var3

def add4(p):
    for num4 in p:
        global var4
        var4 = int(var4) + int(num4)
    return var4

d = add1(m)
e = add2(n)
f = add3(o)
g = add4(p)
li = [d, e, f, g]

maximum = -1000
for num in li:
    if num > maximum:
        maximum = num

if maximum == sum1:
    print(m)
if maximum == sum2:
    print(n)
if maximum == sum3:
    print(o)
if maximum == sum4:
    print(p)