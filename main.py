from turtle import Turtle, Screen
import turtle_blueprint

screen = Screen()
screen.setup(width=500,height=400)
turtle_colors = ["red","green","purple","black","orange","blue"]
user_input = screen.textinput(title="Place Your Bets",prompt="Which Turtle will win the Race? "
                                                             "\nChoose one of the colors(red,grren,purple,black,orange,blue:")

turtle_position = -100
for color in turtle_colors:
    hell = Turtle(shape="turtle")
    hell.color(color)
    hell.penup()
    hell.goto(-230, turtle_position)
    turtle_position+=40


screen.exitonclick()

