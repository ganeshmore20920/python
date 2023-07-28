import re
pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
new_pattern = r"\1\2\3"
user = input()
result = re.sub(pattern, new_pattern,user)
print(result)