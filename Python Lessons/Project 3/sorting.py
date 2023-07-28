a = input()
lower = []
cap = []
even = []
odd = []
for i in range(len(a)):
    if(a[i].isupper()):
        cap.append(a[i])
    elif(a[i].islower()):
        lower.append(a[i])
    elif(a[i].isdigit()):
        if(int(a[i]) %2 == 0):
            even.append(int(a[i]))
        else:
            odd.append(int(a[i]))
x = sorted(lower)+sorted(cap)+sorted(odd)+sorted(even)
print(*x,sep="")