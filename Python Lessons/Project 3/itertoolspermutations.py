# >>> from itertools import permutations
# >>> print permutations(['1','2','3'])
# <itertools.permutations object at 0x02A45210>
# >>> 
# >>> print list(permutations(['1','2','3']))
# [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
# >>> 
# >>> print list(permutations(['1','2','3'],2))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
# >>>
# >>> print list(permutations('abc',3))
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
from itertools import permutations
a = input().split()
b,c = str(a[0]),int(a[1])
# print(list(permutations(*b,c)))
d = tuple(sorted(permutations(b,c)))
for i in d:
    print(''.join(i))
# for i in range(len(b)*(len(b)-1)):
    # print(d[i][0],end="",)
    # print(d[i][1])

# def funct(x,y,z):
#     print(x,end="")
#     print(y,end="")
#     print(z)
# i = 0
# while(i < len(d)):
#     # print(d[i])
#     funct(d[i])
#     i += 1