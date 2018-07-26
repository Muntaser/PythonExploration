#
# Author: Muntaser Khan
#
# threelines3.py
#

import turtle


def draw_line_2(t,height):
    t.left(90)  # turn by 90 degrees
    t.forward(height)
    t.setheading(0.0)
    t.up()
    t.goto(0,0)
    t.down()

def draw_3_lines(t,height,gap):
    x = 0
    draw_line_2(t, height)
    t.up()
    x = x + gap
    t.goto(x, 0)
    t.down()
    draw_line_2(t, height)
    t.up()
    x = x + gap
    t.goto(x, 0)
    t.down()
    draw_line_2(t, height)

def main():
    wn = turtle.Screen()  # Set up the window and its attributes
    wn.bgcolor("lightgreen")
    turtle.home()
    tess = turtle.Turtle()  # create tess and set some attributes
    tess.color("blue")
    tess.pensize(3)
    height = int(input("Enter the height of the lines:"))
    gap = int(input("Enter the gap between lines:"))

    draw_3_lines(tess, height, gap)

    wn.exitonclick()

main()
