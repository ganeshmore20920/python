# cube = lambda x : x**3
# def fibonacci(n):
#     lst = []
#     if(n==0):
#         lst.append(0)
#         if(n==1 or n==2):
#             lst.append(1)
#             if(n>2):
#                 lst.append(fibonacci(n-1)+fibonacci(n-2))
#     return lst

# n = int(input())
# print(list(map(cube, fibonacci(n))))
# cube = lambda x: x**3 # complete the lambda function 
def fibo(y):
    return fibo(y-1)+fibo(y-2)
def fibonacci(n):
    result = []
    if(n>=0):
        result.append(0)
    if(n>=1 or n>=2):
        result.append(1)
    if(n>2):
        for i in range(2,n+1):
            result.append(fibo(i))
    return result
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    # print(list(map(cube, fibonacci(n))))
    print(fibonacci(n))