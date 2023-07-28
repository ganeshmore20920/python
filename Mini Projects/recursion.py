import time
def rec(x):
    x = x + 1
    print(x)
    time.sleep(1)
    rec(x)
rec(1)