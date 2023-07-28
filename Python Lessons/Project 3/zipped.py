# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
st1 = list(map(float, input().split()) for _ in range(m))
st = list(zip(*st1))
for i in range(n):
    s = sum(st[i]) / m
    print(s)