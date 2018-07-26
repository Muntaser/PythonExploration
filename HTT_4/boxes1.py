#
# Author: Muntaser Khan
#
# boxes1.py
#
import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")

turtle.home()

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.pensize(5)


alex = turtle.Turtle()           # create alex

center = [0,0]
side = 100
xPt=center[0]-side/2
yPt=center[1]+side/2
alex.up()
alex.goto(xPt, yPt)
alex.down()
for i in range(4):
    alex.forward(side)
    alex.right(90)

side = 80
xPt = center[0] - side / 2
yPt = center[1] + side / 2
alex.up()
alex.goto(xPt, yPt)
alex.down()
for i in range(4):
    alex.forward(side)
    alex.right(90)

wn.exitonclick()