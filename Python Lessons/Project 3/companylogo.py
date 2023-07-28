from collections import Counter
inp = sorted(input())
c = Counter(inp)
for k,v in c.most_common(3):
    print(k,v)