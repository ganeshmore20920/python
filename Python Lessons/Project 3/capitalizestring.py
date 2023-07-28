# # s = "1 w 2 r 3g"
# # print(" ".join((s.capitalize() for s in input().strip().split(" "))))
# p = "Hello world"
# def print4():
#     a = p.split()
#     b = list(a)
#     e = []
#     for s in b:
#         c = s.capitalize()
#         e.append(c)
#     x = ' '.join(e)
#     print(x,end="")
# def solve():
#     x3 = print4()
#     return x3
# solve()
# s = input()
# def print4():
#     a = s.split()
#     b = list(a)
#     e = []
#     for v in b:
#         c = v.capitalize()
#         e.append(c)
#     x = ' '.join(e)
#     print(x,end="")
# def solve():
#     x3 = print4()
#     return x3
# solve()
# e = "Hello world"
# g = []
# def solve(s):
#     for x in e.split():
#         p = x.title()
#         g.append(p)
        
# def printf():
#     j = " ".join(g)
#     return j
# print(printf())
import string
s = input()
def solve(s):
    return string.capwords(s,' ')
print(solve(s))