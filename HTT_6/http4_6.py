#
# Python program that asks the user for the number of sides, the length of the side, the color, and the fill color of a regular polygon
#
# Author: Muntaser Khan
#
import turtle

numSides = int(input("Enter the number of sides in polygon: "))
lengthSide = float(input("Enter the length of the side: "))
color = input("Enter the color of the polygon: ")
fillColor = input("Enter the fill color of the polygon: ")

wn = turtle.Screen()
alex = turtle.Turtle()
alex.begin_fill()

for i in range(numSides):
    alex.color(color)
    alex.forward(lengthSide)
    alex.left(360/numSides)

alex.color(fillColor)

alex.end_fill()
wn.exitonclick()