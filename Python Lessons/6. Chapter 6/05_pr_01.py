a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter Third number : "))
d = int(input("Enter fourth number : "))

if (a>b):
    maxnum1 = a
else:
        maxnum1 = b
if (c>d):
    maxnum2 = c
else:
    maxnum2 = d
if (maxnum1 > maxnum2):
    maxnum = maxnum1
else:
    maxnum = maxnum2

print("bigger number amoung given number is ", maxnum)