t = int(input())
for i in range(t):
    n,s = int(input()),list(map(int,input().split(" ")))
    a,b = s[0],s[n-1]
    result = 0
    for x in range(n):
        if(s[x]==a or s[x]==b):
            pass
        elif(s[x]>b):
            result += abs(s[x]-b)
        else:
            result += abs(s[x]-a)
    print(result) 