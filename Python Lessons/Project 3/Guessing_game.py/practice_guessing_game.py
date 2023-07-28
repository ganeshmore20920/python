import random
def number(x):
        A = random.randint(1,x)
        number = 0
        while(number != A):
            number = int(input(f"Enter a number between 1 and {x} : "))
            if(number>A):
                print("Sorry,Your Guess is too high,Try Again ")
            elif(number<A):
                print("Sorry,Your Guess is too low,Try again ")
        
        print(f"Yay, You Guessed the right number : {number}")


number(20)