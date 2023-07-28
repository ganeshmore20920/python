n = int(input())
arr = input().split()

arr.sort()
print(arr)
arr2 = []
for i in arr:
    if i not in arr2:
        arr2.append(i)
print(arr2)
a = len(arr2) - 2
print(arr2[a])