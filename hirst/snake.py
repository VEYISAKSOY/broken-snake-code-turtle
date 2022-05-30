import time
from turtle import Turtle,Screen
import time


screen = Screen()
screen.title("snake game veyis")

screen.bgcolor("Black")
screen.tracer(0)

starting_positions = [(0,0),(-20,0),(-40,0)]

game_on = True
segments = []


for i in starting_positions:
    project=Turtle("square")
    project.penup()
    project.color("white")
    project.goto(i)
    segments.append(project)

def right():
    project.setheading(90)
    project.forward(90)


while game_on:
    screen.update()
    time.sleep(0.3)
    for x in segments:
        x.forward(20)
    right()
def right():
    project.setheading(90)
    project.forward(90)



screen.listen()
screen.onkey(right, "d")


screen.exitonclick()