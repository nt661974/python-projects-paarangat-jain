# using Turtle Programming
import turtle 
length=int(input("Length of Rectangle: "))
height=int(input("Height of Rectangle: "))

t = turtle.Turtle()
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)
t.forward(length)
t.left(90)
t.forward(height)
t.left(90)

turtle.done()
