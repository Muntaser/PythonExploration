#
# Author: Muntaser Khan
#
# triangles.py
#

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.pensize(5)


tess.forward(120)                 # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(120)
tess.left(120)
tess.forward(120)
tess.left(120)                   # complete the triangle

tess.forward(60)

tess.left(120)
tess.forward(60)
tess.right(120)
tess.forward(60)
tess.right(120)
tess.forward(60)


wn.exitonclick()