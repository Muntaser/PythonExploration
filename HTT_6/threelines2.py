#
# Author: Muntaser Khan
#
# threelines2.py
#

import turtle



def draw_line(t):
    t.left(90)  # turn by 90 degrees
    t.forward(200)
    t.setheading(0.0)
    t.up()
    t.goto(0,0)
    t.down()

def draw_3_lines(t):
    draw_line(t)
    t.up()
    t.goto(30, 0)
    t.down()
    draw_line(t)
    t.up()
    t.goto(60, 0)
    t.down()
    draw_line(t)



def main():
    wn = turtle.Screen()  # Set up the window and its attributes
    wn.bgcolor("lightgreen")
    turtle.home()
    tess = turtle.Turtle()  # create tess and set some attributes
    tess.color("blue")
    tess.pensize(3)

    draw_3_lines(tess)

    wn.exitonclick()

main()