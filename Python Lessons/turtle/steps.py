import time
import turtle
eb = turtle.Screen()
eb.bgcolor("light green")
k = turtle.Turtle()
k.color("purple")
a = 1
n = 20
for _ in range(19):
    k.forward(n)
    if(a%2 == 0):
        k.right(90)
    else:
        k.left(90)
    a += 1
k.right(180)
k.forward(200)
k.right(90)
k.forward(200)
k.right(90)
k.forward(20)
time.sleep(10)