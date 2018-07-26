#
# Author: Muntaser Khan
#
# threelines.py
#

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

turtle.home()
tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.pensize(3)

print(tess.position())
tess.left(90)               # turn by 90 degrees
tess.forward(200)

tess.up()
tess.goto(30,0)
tess.down()
# tess.left(90)               # turn by 90 degrees
tess.forward(200)

tess.up()
tess.goto(60,0)
tess.down()
tess.forward(200)
wn.exitonclick()