x = sc.parallelize([1,2,3,4])
y = x.reduce(lambda a,b: a+b)
print(y)
