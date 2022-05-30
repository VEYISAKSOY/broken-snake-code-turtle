from turtle import Turtle, Screen

project = Turtle()
screen = Screen()

project.shape("turtle")
screen.bgcolor("pink")
screen.title(" yooo!")

project.write("hi")

def move_forwards():
  project.forward(10)

def turn_right():
    new_turn = project.heading() - 10
    project.setheading(new_turn)
def turn_left():
    new_turn = project.heading() + 10
    project.setheading(new_turn)




screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="d" , fun=turn_right)
screen.onkey(key="a" , fun=turn_left)


screen.exitonclick()