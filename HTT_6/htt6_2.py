#
# htt6_2.py
#
# Author: Muntaser Khan
#

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

N = int(input("Enter the number of nested squares to draw"))

def draw_square(t,size):
    print(tess.pos())
    for i in range(4):
        tess.forward(size)
        tess.left(90)

size = 20
for j in range(N):
   tess.pensize(3)
   draw_square(tess,size)
   size = size + 20
   tess.penup()
   tess.goto(tess.pos() + (-10, -10))
   tess.pendown()

wn.mainloop()