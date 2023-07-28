import re
pattern = '[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|in)'
inp = input()
print(re.search(pattern, inp))
if(re.search(pattern , inp)):
    print("valid email")
else:
    print("Invalid email")