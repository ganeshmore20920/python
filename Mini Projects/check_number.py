import re

N = int(input())
for i in range(0, N):
    if(re.match(r'[789]\d{9}$', input())):
        print('YES')  
    else:
        print('NO') 
