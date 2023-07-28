# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
t = int(input())
while(t>0):
    n = int(input())
    l = list(map(int, input().split()))
    lst = deque(l)
    rm = lst.pop()
    lm = lst.popleft()
    csv = lm if lm>rm else rm
    lp = -1
    flag = False
    while(len(lst)>0):
        if(lm>=rm and lm<=csv):
            csv = lm
            lm = lst.popleft()
            latest = lm
        elif(rm>lm and rm<=csv):
            csv = rm
            rm = lst.pop()
            latest = rm
        else:
            flag = True
            break
    if(flag or latest>csv):
        print("No")
    else:
        print("Yes")
    t-=1

"""Input (stdin)
2
6
4 3 2 1 3 4
3
1 3 2

Your Output (stdout)
Yes
No"""