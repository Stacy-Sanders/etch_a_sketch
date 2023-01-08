from turtle import Turtle, Screen

tator = Turtle()
screen = Screen()


def move_forward():
    tator.forward(20)


def move_backward():
    tator.backward(20)


def counter_clockwise():
    # new_heading = tator.heading() + 10
    # tator.setheading(new_heading)
    tator.lt(10)


def clockwise():
    # new_heading = tator.heading() - 10
    # tator.setheading(new_heading)
    tator.rt(10)


def return_home():
    tator.home()
    tator.clear()


screen.listen()

screen.onkey(key="w", fun=move_forward)  # screen.onkey(move_forward, "w")
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=return_home)

screen.exitonclick()
