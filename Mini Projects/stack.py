def push():
    res = int(input())
    a.append(res)
def pop():
    a.pop()
a = []
print("length of list is 6.")
while(len(a)<=5):
    print("Enter 1 for push, 2 for pop operation and X to exit : ", end=" ")
    b = input()
    if(b == "1"):
        push()
    elif(b == "2"):
        pop()
    elif(b=="x" or b == "X"):
        break
    else:
        print("Invalid Input")
print(a)
if(len(a)<6):
    print("Hence You leaved stack in between, length of stack reduced to :",len(a))