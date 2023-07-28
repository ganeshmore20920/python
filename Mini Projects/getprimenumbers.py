# def luckyDrawTest(tokenNumber):
#     stri = str(tokenNumber)
#     lst = list(stri)
#     lend = len(stri)  
#     sum2 = int(lst[lend-2])+int(lst[lend-1])
#     if(sum2==3 or sum2==8):
#         return "Lucky Draw winner"
#     else:
#         return "Not a Lucky Draw winner"

# print(luckyDrawTest(1021))

# from collections import deque
# def letterCombinationsUtil(number, n, table):
#     list = []
#     q = deque()
#     q.append("")
#     while len(q) != 0:
#         s = q.pop()
#         if len(s) == n:
#             list.append(s)
#         else:
#             for letter in table[number[len(s)]]:
#                 q.append(s + letter)
#     return list
# def letterCombinations(number):
#     number2 = [int(x) for x in str(number)]
#     n = len(str(number))
#     table = ["0", "1", "abc", "def", "ghi", "jkl",
#              "mno", "pqrs", "tuv", "wxyz"]
#     list = letterCombinationsUtil(number2, n, table)
#     s = ""
#     for word in list:
#         s += word + " "
#     return 
# print(letterCombinations(23))

def letterCombinations(number):
    table = ["0", "1", "abc", "def", "ghi", "jkl","mno", "pqrs", "tuv", "wxyz"]
    lst = [int(x) for x in str(number)]
    result = ""
    for a in table[lst[0]]:
        for b in table[lst[1]]:
            result += a+b+" "
    print(result)

letterCombinations(24)