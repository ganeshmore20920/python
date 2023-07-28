# # Enter your code here. Read input from STDIN. Print output to STDOUT
# a = int(input())
# b = list(set(list(input().split())))
# c = int(input())
# d = list(set(list(input().split())))
# e = []
# for i in range(len(b)):
#     if(b[i] != d[i]):
#         e.append(b[i])
#         e.append(d[i])
# x = sorted(map(int, list(set(e))), reverse=True)
# for j in range(len(e)):
#     print(x[j])
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = set(list(map(int, input().split())))
c = int(input())
d = set(list(map(int, input().split())))
e = b.difference(d)
F = d.difference(b)
x = sorted(list(e.union(F)))
for i in range(len(x)):
    print(x[i])
