from collections import OrderedDict
string = input()
k = int(input())


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))
# def merge_the_tools(string, k):
#     a = list(string)
#     b = len(a)
#     # print(b)
#     c = (len(a)+1)//k
#     # print(c)
#     for i in range(0,b,k):
#         f = a[i:i+k]
#         # print(f)
#         res = []
#         [res.append(x) for x in f if x not in res]
#         # g = list(set(f))
#         # print(g)
#         print(''.join(res[0:2]))
merge_the_tools(string,k)