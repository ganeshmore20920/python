t = int(input())
for a in range(t):
    p,q,n = map(int, input().split(" "))
    z = 2
    for x in range(n-2):
        s = sum(list(map(int, bin(z)[2:])))
        z = p*s + q
    print(sum(list(map(int,bin(z)[2:]))))