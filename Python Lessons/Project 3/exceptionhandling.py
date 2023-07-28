n = int(input())
for i in range(n):
    a,b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as f:
        print("Error Code:",f)

import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except:
        ans = False
    print(ans)