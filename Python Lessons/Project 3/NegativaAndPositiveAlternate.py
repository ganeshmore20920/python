from cgi import print_arguments


arr2 = list(map(int, input().split()))
def Rearrange(arr):
    length = len(arr)
    # len2 = []
    a = ""
    for i in range(0, length , 2):
        if(arr[i] > arr[i+1]):
            a += str(arr[i+1]) + " " + str(arr[i]) + " " 
        else:
            a += str(arr[i]) + " " + str(arr[i+1]) + " " 
    return a

print(Rearrange(arr2))