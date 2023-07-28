l = int(input())
r = int(input())
def count(a,b):
    counting = 0
    for i in range(a,b):
        x = str(i)
        if(("2" in x and "3" in x) or ("4" in x and "5" in x) or ("6" in x and "7" in x)):
            counting = i
    return counting
print(count(l,r))