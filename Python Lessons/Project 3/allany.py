# a , lst = int(input()), list(map(int, input().split()))
# # print(all([lst[i]>0 for i in range(a) or if(n == n[:: -1])]))
# b = any[[lst[i]>0 for i in range(a)]]
# # c = [True if(a == a[::-1]) else False)]
# # print(all([[lst[i]>0 for i in range(a)] or True if(a== a[::-1])]))

# a , lst = int(input()), list(map(int, input().split()))
# print(all([i>0 for i in lst , any([str(x) == str(x)[::-1] for x in str(a)])]))


N = int(input())
numbers = list(map(int, input().split()))
print(all([x > 0 for x in numbers]) and any([str(x) == str(x)[::-1] for x in numbers]))

n, lst = int(input()), list(map(int, input().split()))
print(all([x>0 for x in lst]) and any([str(x) == str(x)[::-1] for x in lst]))