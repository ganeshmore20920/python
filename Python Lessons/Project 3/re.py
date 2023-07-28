# # Enter your code here. Read input from STDIN. Print output to STDOUT
# import re
# n = int(input())
# for _ in range(n):
#     a = input()
#     print(bool(re.search(r"str([0-9].[0-9])","a")))
from fractions import Fraction


a = Fraction(*map(int, input().split()))
print(a)