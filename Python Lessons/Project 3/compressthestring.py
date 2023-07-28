# from itertools import groupby

# for k, c in groupby(input()):
#     print("(%d, %d)" % (len(list(c)), int(k)), end=' ')
from itertools import groupby
s = str(input())
t = [list(g) for k,g in groupby(s)]
for i in t:
    print((len(i), int(i[0])),end=(' '))
print(t)