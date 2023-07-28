n = int(input())
k = int(input())
if(len(str(n))==k):
    print("True",end=" ")
    print(k)
else:
    print("False", end=" ")
    print(len(str(n)))
