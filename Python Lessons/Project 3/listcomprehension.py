#numbers = [2**i for i in range(1,6)]
#print(numbers)
#num = [i**2 for i in range(1,7)]
#print(num)
b = []
def insert(p,e):
    b.insert(p,e)
    print(b)
a = list(input().split())
x = int(a[1])
y = int(a[2])
insert(x,y)