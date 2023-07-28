def Findsum(a,b):
    return a+b

def FindProduct(a,b):
    return a*b

def Pyramid(number):
    for i in range(1,number+1):
        for _ in range(1,i):
            print("*",end="")
        print()

Pyramid(15)