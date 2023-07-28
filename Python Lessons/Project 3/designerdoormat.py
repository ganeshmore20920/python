# a = input().split()
# n = int(a[0])
# m = int(a[1])
# dot = ".|."
# x = 1
# lines = m//n
# dot2 = lines*7.5
# def upper():
#     for i in range(1,lines+1):
#         dot2 = int(lines*7.5)
       
#         print((dot*x).center(dot2,'-'))
#         x = x + 2
#         dot2 = dot2 - 7.5
# upper()



# N, M = map(int,input().split())
# for i in range(1,N,2): 
#     print((i * ".|.").center(M, "-"))
# print("WELCOME".center(M,"-"))
# for i in range(N-2,-1,-2): 
#     print((i * ".|.").center(M, "-"))
import time
a = input().split()
n = int(a[0])
m = int(a[1])
#head
for i in range(1,n,2):
    print((i*".|.").center(m,'-'))
    time.sleep(1)
#welcome part
print('WELCOME'.center(m,'-'))
time.sleep(1)
#leg part
for i in range(n-2,-1,-2):
    print((i*'.|.').center(m,'-'))
    time.sleep(1)