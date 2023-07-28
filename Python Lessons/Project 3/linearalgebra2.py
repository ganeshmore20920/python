import numpy
N= input()
arr= numpy.array( [(map(float, input().split())) for i in range(N)])
print(numpy.linalg.det(arr))