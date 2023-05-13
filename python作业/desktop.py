from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("white")

for i in range(20):
    x = randint(-300, 300)
    y = randint(-300, 300)
    turtle = Turtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turtle.fillcolor(r/255, g/255, b/255)
    turtle.begin_fill()
    for j in range(5):
        turtle.forward(randint(30, 40))
        turtle.right(144)
    turtle.end_fill()

screen.mainloop()

