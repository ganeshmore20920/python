# p = [['harry',35],['ganesh',65],['sand',85]]
# for i in range(2):
#     print(p[i][0][0])
# c = 'H'()
# print(c*3)
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
N= int(input())
d= OrderedDict()
for i in range(N):
    item = input().split()
    itemPrice= int(item[-1])
    itemName= " ".join(item[:-1])
    if d.get(itemName):                      # .get is used to check if itemName already exists
       d[itemName] += itemPrice
    else:
       d[itemName] = itemPrice
for i in d.keys():
    print(i,d[i])