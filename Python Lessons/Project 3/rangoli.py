import time
def print_rangoli(size):
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size-1,-size,-1):
        x = abs(i)
        line = a[size-1:x:-1] + a[x:size]
        time.sleep(1)
        print("--"*x + '-'.join(line) + "--"*x)

# def print_rangoli(size):
#     myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
#     for i in range(size-1, -size, -1):
#         x = abs(i)
#         if x >= 0:
#             line = myStr[size:x:-1]+myStr[x:size]
#             print ("--"*x+ '-'.join(line)+"--"*x)

n = int(input())
print_rangoli(n)