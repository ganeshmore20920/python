# Enter your code here. Read input from STDIN. Print output to STDOUTn
"""n = int(input())
a = set(list(map(int,input().split())))
o = int(input())
x = 0
for _ in range(o):
    s = list(input().split())
    if(len(s)>=2):
        x = int(s[1])
        
    if(s[0] == 'remove'):
        a.remove(x)
    elif(s[0] == 'pop'):
        a.pop()
    elif(s[0] == 'discard'):
        a.discard(x)
print(sum(a))"""
"""a = set([1,2,3,4,5,6])
b = set([4,5,6,7,8,9])
a = a.intersection(b)
a = a.union(b)
print(sum(a))
c,d = input().split()
print(c,d)"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
"""n = int(input())
s = set(list(map(int, input().split())))
op = int(input())
for i in range(op):
    operation, number = input().split()
    a = set(list(map(int, input().split())))
    if(operation == "intersection_update"):
        s = s.intersection(a)
    elif(operation == "update"):
        s = s.update(a)
    elif(operation == "symmetric_difference_update"):
        s = s.symmetric_difference_update(a)
    elif(operation == "difference_update"):
        s = s.difference_update(a)
print(sum(s))"""

"""a, b = int(input()) , set(map(int, input().split()))
print(a)
print(b)"""

n1 , n2 = map(int, input().split())
print(n1, n2)