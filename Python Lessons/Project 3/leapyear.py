def is_leap(year):
    a = year%4
    b = year%100
    c = year%400
    if(a == 0 and b == 0 and c == 0):
        return True
    elif(b == 0 and c == 0) and (a == 0):
        return True
    else:
        return False
year = int(input())
print(is_leap(year))