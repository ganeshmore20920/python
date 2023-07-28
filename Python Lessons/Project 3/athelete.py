from operator import itemgetter
nm = list(map(int, input().split()))
n,m = nm[0], nm[1]
arr = []
for i in range(n):
    arr += [list(map(int, input().split()))]
k = int(input())
result = sorted(arr,key= itemgetter(k))
for i in result:
    print(*i)