from itertools import combinations, permutations
a = input().split()
b,c = str(a[0]),int(a[1])
# print(list(permutations(*b,c)))
# d = tuple(sorted(combinations(b,c)))

for j in range(1,c+1):
    for i in combinations(sorted(b,j)):
        print(''.join(i))