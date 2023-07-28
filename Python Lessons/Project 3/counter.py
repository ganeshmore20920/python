# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
noofshoes = int(input())
sizes = list(map(int,input().split()))
customers = int(input())
price = []
for i in range(customers):
    a = list(map(int,input().split()))
    if a[0] in sizes:
        price.append(a[1])
        sizes.remove(a[0])
print(sum(price))     