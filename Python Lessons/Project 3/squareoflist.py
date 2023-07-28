a = [1,2,3,4,5]
square_num = []
square = lambda x: x**2
for n in a:
    square_num.append(square(n))
print(square_num)

s2 = list(map(lambda n : n**2 , a))
print(s2)