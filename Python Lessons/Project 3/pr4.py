from typing import Counter


def checking(a,b):
    Counter= 0
    for i in range(len(a)-len(b)+1):
        if(a[i:i+len(b)] == b):
            Counter += 1
    return Counter

a = input().strip()
b = input().strip()
count = checking(a,b)
print(count)