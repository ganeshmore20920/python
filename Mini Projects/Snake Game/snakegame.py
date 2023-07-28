import pygame
import sys
import sys
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()
#we will declare global constant defination

speed = 0.30
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE #WE WILL KEEP BOTH FOOD AND SNAKE SAME
SEPARATION = 10 #DISTANCE BETWEEEN APPLES OF SNAKE
SCREEN_HEIGHT = 600
SCREEN_WEIGHT = 800
FPS = 25
KEY = {"UP":1 , "DOWN":2 , "LEFT": 3 , "RIGHT": 4}

#WE WILL INITIATE SCREEN
screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_HEIGHT),pygame.HWSURFACE)
#WE HAVE USED HW SURFACE WHICH STANDS FOR HARDWARE SURFACE REFERS TO USING MEMORY on the video card for storing
#draws as opposed to main memory

#Resources
score_font = pygame.font.Font(None,38)
score_numb_font = pygame.font.Font(None, 28)
game_over_font = score_numb_font
score_msg = score_font.render("Score : ", 1,pygame.color("Green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0,0,0) # we will fill background as black
black = pygame.Color(0,0,0)

# for clock at the left corner
gameclock = pygame.time.Clock()

#we will define keys

def getkeys():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            if event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            if event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            if event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]
            #FOR EXIT
            elif event.key == pygame.K_ESCAPE:
                return "exit"
            # if we want to contiue playing again
            elif event.key == pygame.K_y:
                return "yes"
            #if we don't want to play game
            elif event.key == pygame.K_n:
                return "no"
        if event.type == pygame.QUIT:
            sys.exit(0)

def endgame():
    massage = game_over_font.render("Game Over",1, pygame.Color("white"))
    massage_play_again = play_again_font.render("Play Again ? (Y/N)", 1, pygame.Color("green"))
    screen.blit(massage,(320,240))
    screen_blit(massage_play_again,(320+12,240+40))

    pygame.display.flip()
    pygame.display.update()

    mKey = getKey()
    while(mKey != "exit"):
        if(mKey == "yes"):
            main()
        elif(mKey == "no"):
            break
        mKey = getKey()
        gameClock.tick(FPS)
    sys.exit(0)

