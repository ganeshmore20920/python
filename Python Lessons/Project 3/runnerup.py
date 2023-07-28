n = int(input())
arr=[]
arr.append(input().split())
c=arr[0]
d=[]
for i in range (len(c)):
    d.append(int(c[i]))
    x=sorted(d,reverse=True)
for i in range (len(x)):
    if (x[0]==x[i+1]):
      continue
    else:
        print(x[i+1])
    break