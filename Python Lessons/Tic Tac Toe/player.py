import math
import random

class player:               #base player class
    def __init__(self,letter):
        #letter is x or o
        self.letter = letter
    #we want all players to get there next move given the game
    def get_move(self,game):
        pass

class randomcomputerplayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        pass 
class humanplayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        pass