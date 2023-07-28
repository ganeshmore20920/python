import re
m = re.findall(r'(?<=[qwrtypsdfghjklmnbvcxz])([aeiou]{2,})(?=[qwrtypsdfghjklmnbvcxz])', input().strip(), re.IGNORECASE)
# m = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)
if m:
    for s in m:
        print(s)
else:
    print(-1)