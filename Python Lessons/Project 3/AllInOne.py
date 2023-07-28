#title name
dictionary = {
    1 : "Print Hello World"
}
print('\n'.join("{}) {}".format(k, v) for k, v in dictionary.items()))
user = int(input("Enter chapter number to get information about the chapter : "))
#function
def printfuction():
    print("""Here is a sample line of code that can be executed in Python:\nprint("Hello, World!")\nYou can just as easily store a string as a variable and then print it to stdout:\nmy_string = "Hello, World!"\nprint(my_string)\nThe above code will print Hello, World! on your screen""")

#function calling
if(user == 1):
    print(printfuction())