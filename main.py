from turtle import Turtle, Screen
import turtle_blueprint
import random

screen = Screen()
screen.setup(width=500,height=400)
turtle_colors = ["red","green","purple","black","orange","blue"]
user_input = screen.textinput(title="Place Your Bets",prompt="Which Turtle will win the Race? "
                                                             "\nChoose one of the colors(red,grren,purple,black,orange,blue:")

all_turtles = []
is_game_on = False

turtle_position = -100
for color in turtle_colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, turtle_position)
    turtle_position+=40
    all_turtles.append(new_turtle)

if user_input:
    is_game_on=True

while is_game_on:
    for turtle in all_turtles:
        turtle.speed(6)
        move_forward = random.randint(0, 10)
        turtle.forward(move_forward)
        if turtle.xcor()>=235:
            is_game_on=False
            winner = turtle.pencolor()
            if user_input == winner:
                print(f"You WON!!!! The winner is {winner}")
            else:
                print(f"You LOST! The winner is {winner}")


screen.exitonclick()

