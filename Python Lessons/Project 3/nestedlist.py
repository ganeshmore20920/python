n = int(input())
a = []
for i in range(n):
    a.append(input())
    a.append(float(input()))
o = list(filter(lambda n : n%2 == 1 , n))
e = list(filter(lambda n : n%2 == 0 , n))
o1 = max(o)
print(o1)

# a = input()
# b = int(input())
# print(a + str(b))