import random

def play():
    user = input("Enter 'r' for rock \n 'p' for paper \n 's' for scissors : ")
    comp = random.choice(['r' , 'p' , 's'])
    if(user == comp):
        return 'Its tie'
    if win(user,comp):
        return "You won :) "
    return "You lost ! "

def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())