n = int(input())
email = []
for _ in range(n):
    email.append(input())
print(email)

def filterlist(e):
    return list(filter(verify,e))

def verify(s):
    try:
        username , url = s.split('@')
        website, extension = url.split('.')
        print(username,url,website,extension)
    except ValueError:
        return False
    
    if username.replace('-','').replace('_','').isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension)>3 :
        return False
    else:
        return True
print(sorted(filterlist(email)))