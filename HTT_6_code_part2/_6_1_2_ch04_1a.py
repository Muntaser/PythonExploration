#
# HTT Ch 6 code example:
#
# Section 6.1, example 2: ch04_1a
#
''' a docstring for the entire script (module) '''

import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()          # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()        # create alex
drawSquare(alex, 50)          # Call the function to draw the square

alex.penup()
alex.goto(100,100)
alex.pendown()

drawSquare(alex,75)           # Draw another square

print (drawSquare.__doc__)    # can access docstring as function attribute
# print (doc(drawSquare))

wn.exitonclick()
