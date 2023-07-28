def addfive(nums):
    return nums + 5
a = int(input("Enter number one by one : "))
b = int(input())
c = int(input())
d = int(input())
e = [a, b, c, d]
result = list(map(addfive,e))
print(result)