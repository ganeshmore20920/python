import random

def number(x):
    a = random.randint(1,x)
    number = 0
    while(number != a):
        number = int(input(f"Enter a number between 1 and {x} : "))
        if(number>a):
            print("sorry, your guess is too high")
        elif(number<a):
            print("sorry, your guess is too low ")

    print("Yay, You guessed the right number!!")

number(20)