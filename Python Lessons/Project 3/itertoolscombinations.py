# from itertools import combinations
# a = input().split()
# b = int(a[1]) + 1
# for i in range(1,b):
#     for j in combinations(sorted(a[0]), i):
#         print(''.join(j))

from itertools import combinations
string = input().split()
length = int(string[1]) + 1
for i in range(1,length):
    for j in combinations(sorted(string[0]),i):
        print(''.join(j))