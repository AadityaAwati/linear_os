import random
import turtle
from turtle import *

color_list = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64), (119, 46, 39), (48, 65, 61)]
turtle_object = Turtle()
screen = Screen()
x = 1
y = 3
times = 1
turtle_object.hideturtle()
turtle_object.penup()
turtle_object.setheading(225)
turtle_object.forward(250)
turtle_object.setheading(0)
number_of_dots = 100
turtle_object.speed("fastest")
for dot_count in range(1,number_of_dots + 1):
    turtle.colormode(255)
    turtle_object.dot(20, random.choice(color_list))
    turtle_object.forward(50)
    if dot_count % 10 == 0:
        turtle_object.setheading(90)
        turtle_object.forward(50)
        turtle_object.setheading(180)
        turtle_object.forward(500)
        turtle_object.setheading(0)


screen.exitonclick()











