a23 = input("Enter Your Name : ")
letter = 'hello' + f'{a23}' + '\n\t Welcome to python program \n how are you ' + f'{a23}'
print(letter)
b23 = input("Enter another name : ")
print(letter.replace("a23","b23"))
print(letter.find("Welcome"))