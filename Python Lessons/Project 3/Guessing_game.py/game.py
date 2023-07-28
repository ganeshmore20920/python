import random

def number(x):
    a = random.randint(10,30)
    x = 10
    while(a != x):
        x = int(input(f'Enter a value between 10 and 30 : '))
        if(x>a):
            print("Given value is high, try to put lower value ")
        elif(x<a):
            print("Given value is low, try to give higher value ")
    print(f"Yay, You guessed right number : {x}")
number(30)