# # Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import OrderedDict
# od = {}
# n = int(input())
# for _ in range(n):
#     a = list(input().split())
#     b = len(a)
#     od[a[0:(b-2)]] = a[(b-1)]

# print('\n'.join("{} {}".format(k, v) for k, v in od.items()))
from collections import *
n = int(input('how much items do you have : '))
d = OrderedDict()
for i in range(n):
    item = input("Enter item name and price of it : ").split()
    itemname = "".join(item[:-1])
    itemprice = int(item[-1])
    if d.get(itemname): #d.get is used to add existing item price
        d[itemname] += itemprice
    else:
        d[itemname] = itemprice
# print('/n'.join("{} {}".format(k,v) for k, v in d.items()))
print("final items bill is : ")
for i in d.keys():
    print(i, d[i])
p = 0
for j in d.keys():
    p += d[j]
print("total bill is : ",p)