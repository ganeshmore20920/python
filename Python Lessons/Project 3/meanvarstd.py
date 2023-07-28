# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n,m = map(int, input().split())
res = []
for _ in range(n):
    res.append(list(map(int, input().split())))
my_array = numpy.array(res)
numpy.set_printoptions(legacy = '1.13')
a = numpy.mean(my_array, axis = 1)
print(numpy.var(my_array, axis = 0))
print(numpy.std(my_array, axis = None))