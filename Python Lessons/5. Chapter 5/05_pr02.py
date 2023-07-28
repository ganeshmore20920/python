a = int(input("enter a year to check its leap year or not : "))
b = a%4
c = a%100
d = a%400

if(b == 0):
    if(c == 0):
        if(d == 0):
            print("Given year is leap year")
else:
    print("Given year is not leap year")