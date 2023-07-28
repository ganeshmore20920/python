z = int(input("Enter a number which you going to search : "))
n = list(map(int, input().split()))
x = n[0]
y = n[len(n)]
def find(x , y , z):
    if(x == z):
        return x
    elif(y == z):
        return y
    def low(x, y, z):
        