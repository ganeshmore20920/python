if __name__ == '__main__':
    N = int(input())
    b = []
    def insert(p,e):
        b.insert(p,e)
    def append(x):
        b.append(x)
    def remove(y):
        b.remove(y)
    def pop(z):
        b.pop(z)
    def sort():
        b.sort()
    def reverse():
        b.reverse()
    def prnt():
        print(b)
    for i in range(N):
        a = list(input().split())
        if(a[0] == 'insert'):
            u = int(a[1])
            v = int(a[2])
            insert(u,v)
        if(a[0] == 'append'):
            ap1 = int(a[1])
            append(ap1)
        if(a[0] == 'remove'):
            ar1 = int(a[1])
            remove(ar1)
        if(a[0] == 'pop'):
            apo1 = 3
            pop(apo1)
        if(a[0] == 'sort'):
            sort()
        if(a[0] == 'reverse'):
            reverse()
        if(a[0] == 'print'):
            prnt()