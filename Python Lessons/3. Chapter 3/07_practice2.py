name = input("Enter the name: ")
date = input("Enter the date: ")

template = '''
Dear name1,
you are selected
date1
'''

print(template.replace('name1', name).replace('date1', date))