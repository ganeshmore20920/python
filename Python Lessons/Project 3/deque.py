# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import deque
# d = deque()
# n = int(input())
# for i in range(n):
#     a = input().split()
#     if(a[0]=="append"):
#         d.append(int(a[1]))
#     elif(a[0]=="appendleft"):
#         d.appendleft(int(a[1]))
#     elif(a[0]== "pop"):
#         d.pop()
#     elif(a[0]== "popleft"):
#         d.popleft()
# # print(v for v in deque())

# print(' '.join(d))
from collections import deque

d = deque()
for i in range(int(input())):
    command = input().split()
    if command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'appendleft':
        d.appendleft(command[1])
    elif command[0] == 'pop':
        d.pop()
    else:
        d.popleft()
print(' '.join(d))