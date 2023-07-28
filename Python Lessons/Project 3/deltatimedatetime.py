from datetime import datetime
n = int(input())
def delta(t1,t2):
    form = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, form)
    t2 = datetime.strptime(t2, form)
    return str(int(abs((t1-t2).total_seconds())))
for _ in range(n):
    t1 = input()
    t2 = input()
    result = delta(t1,t2)
    print(result)