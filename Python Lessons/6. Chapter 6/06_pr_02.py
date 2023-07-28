a = int(input("Enter marks of sub. 1 : "))
b = int(input("Enter marks of sub. 2 : "))
c = int(input("Enter marks of sub. 3 : "))
d = int(input("Enter marks of sub. 4 : "))
e = int(input("Enter marks of sub. 5 : "))
f = int(input("Enter marks of sub. 6 : "))

overall = (a+b+c+d+e+f)/6

if (overall>=40):
    if (a >= 33 and b >= 33 and c >= 33 and d >= 33 and e >= 33 and f >= 33 ):
        print("You are passed in all subjects")
    else:
        print("You are failed in some of subjects")
else:
    print("You are failed due to overall marks ")