from turtle import Turtle, Screen
import turtle_blueprint

screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput(title="Place Your Bets",prompt="Which Turtle will win the Race? Type(red, green or blue): ")
turtle_colors = ["red","green","purple","yellow","orange","blue"]

hell=Turtle(shape="turtle")
hell.penup()
hell.goto(-230,-120)







screen.exitonclick()

