# # Enter your code here. Read input from STDIN. Print output to STDOUT
# import numpy
# from numpy import array
# l , m = map(int, input().split())
# a = [map(int, input().split()) for _ in range(l)]
# array = numpy.array(a)
# array = numpy.reshape(array , (l,m))
# min1 = numpy.min(array , axis = 1)
# print(numpy.max(min1))

# import numpy 
# N,M = map(int, input().split())
# array= numpy.array( [map(int, input().split()) for i in range(N)])
# Min= numpy.min(array, axis=1)
# print(numpy.max(Min))

# below code works correctly

# import numpy
# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     a += map(int, input().split())
# a = numpy.array(a)
# a = numpy.reshape(a, (n,m))
# a_min = numpy.min(a, axis = 1)
# print(numpy.max(a_min))