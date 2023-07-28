def ascending(ls):
    n = len(ls)
    status = False
    if(n<=1):
        return True
    for i in range(0, n-1):
        if(ls[i] <= ls[i-1]):
            status = True
        else:
            status = False
            break
    return status

ls = input().replace(" ","").split(",")
print(ascending(ls))