import time
from turtle import Turtle, Screen
import random
# todo - make it so multiple people can place bets!
# todo -maybe add like betting
# todo - fix an error where 2 colors win
screen = Screen()
screen.setup(width=500,height=400)
turtle_colors = ["red","green","purple","black","orange","blue","yellow"]
user_input = screen.textinput(title="Place Your Bets",prompt="Which Turtle will win the Race? "
                                                             "\nChoose one of the colors(red,green,purple,black,orange,blue,yellow)")
correct_input = True
# check if the input is valid, as turtle doesn't have window with buttons to select color
while correct_input:
    if user_input is None:
        print("The race is Cancelled")
        exit()
    elif user_input not in turtle_colors:
        print("invalid input, try again!")
        user_input = screen.textinput(title="Place Your Bets", prompt="Which Turtle will win the Race? "
                                                                      "\nChoose one of the colors(red,grren,purple,black,orange,blue)")
    else:
        correct_input = False

all_turtles = []
turtle_position = -100
#creating turtles
for color in turtle_colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, turtle_position)
    turtle_position+=40
    all_turtles.append(new_turtle)

is_game_on = True
#unit we get a winner we race!
while is_game_on:
    for turtle in all_turtles:
        turtle.speed(6)
        move_forward = random.randint(0, 10)
        turtle.forward(move_forward)
        if turtle.xcor()>=230:
            is_game_on=False
            winner = turtle.pencolor()
            if user_input == winner:
                print(f"You WON!!!! The winner is {winner}")
            else:
                print(f"You LOST! The winner is {winner}")

screen.exitonclick()
time.sleep(5)
screen.bye()
