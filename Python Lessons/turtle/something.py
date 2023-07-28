# import turtle  #Inside_Out
# wn = turtle.Screen()
# wn.bgcolor("light green")
# skk = turtle.Turtle()
# skk.color("blue")
 
# def sqrfunc(size):
#     for i in range(4): 
#         skk.fd(size)
#         skk.left(90)
#         size = size + 5
#         # for x in range(5):
#             # skk.forward(150)
#             # skk.right(144)
#         skk.circle(80)
 
# sqrfunc(6)
# sqrfunc(26)
# sqrfunc(46)
# sqrfunc(66)
# sqrfunc(86)
# sqrfunc(106)
# sqrfunc(126)
# sqrfunc(146)
# for x in range(5):
#     skk.forward(150)
#     skk.right(144)
# import turtle 
# k = turtle.Turtle()
# s = 0
# for i in range(40):
#     k.forward(5 + s)
#     k.right(90)
#     s += 5
import turtle
k = turtle.Turtle()
b = turtle.Screen()
b.bgcolor("light green")
s = 5
for i in range(20):
    k.circle(s, extent=90)
    s += 5