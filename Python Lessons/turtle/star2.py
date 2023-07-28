import turtle 
col = ('yellow','red','green','white','blue','pink','yellow','red','green','white','blue','pink')
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(30)

for i in range(180):
    t.color(col[i%12])
    t.forward(i*4)
    t.left(150)
    t.width(2)