from itertools import count
l = int(input())
r = int(input())
arr = []
for _ in range(r):
    a = list(map(int, input().split(" ")))
    arr.append(sorted(a))
out = []
for i in range(r):
    dict1 = {item:arr[i].count(item) for item in arr[i]}
    key = []
    value = []
    for k,v in dict1.items():
        x,y = k,v
        key.append(x)
        value.append(y)
    out2 = []
    for _ in range(l):
        out2.append(0)
    for j in range(len(key)):
        for k in range(l):
            if(arr[i][k] == key[j]):
                out2[k] = value[j]
    out.append(out2)

print(out)