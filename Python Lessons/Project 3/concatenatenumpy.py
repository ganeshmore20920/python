import numpy
n, m, a = map(int,input().split())
res = []
for _ in range(n+m):
    res.append(list(map(int,input().split())))
result = numpy.array(res)
print(numpy.concatenate(result,axis = 0))