import turtle
k = turtle.Turtle()
s = 0
for i in range(4):
    k.circle(80)
    k.forward(80+s)
    s += 40