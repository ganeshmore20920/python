# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
l = list()
for _ in range(n):
    l.append(input())
x = Counter(l)
print(len(x))
print(*x.values())

"""Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1"""