price = double(input("Enter the price before inflation : "))
inflation = float(input("Enter the rate of inflation : "))
year = int(input("Enter the total years "))
def cal(x, y , z):
    for _ in range(z):
        x = x * y
    return x
print([price*inflation for _ in range(year)])