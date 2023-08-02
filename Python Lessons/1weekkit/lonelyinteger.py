def lonelyinteger(a):
    b = list(set(a))
    c = True
    index = len(b)-1
    while(True):
        if(b[index]%2 == 0):
            index = index - 1
        else:
            break
    while(True):
        if(a.count(a[index])>1):
            index = index - 1
        else:
            break
    return a[index]
        
        
    
        
    # Write your code here

