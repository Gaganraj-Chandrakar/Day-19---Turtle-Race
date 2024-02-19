from turtle import Turtle, Screen
import easygui
import random

y = 0

class T:
    obj_list = []

    def make_turtle(self):
        turtle_obj = Turtle(shape="turtle", visible=False)
        self.obj_list.append(turtle_obj)

    def set_color(self, i):
        self.obj_list[i].color(colors[i])

    def set_speed(self, speed, i):
        self.obj_list[i].speed(speed)

    def start(self, i):
        global y
        self.obj_list[i].penup()
        y = ((-1) ** (i + 1) * i * 105) + y
        self.obj_list[i].goto(-340, y)

    def delete_turtle(self):
        for turtle in self.obj_list:
            del turtle
        self.obj_list.clear()

new_turtle = T()
screen = Screen()
screen.setup(width=700, height=670)
screen.bgcolor("SkyBlue")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

for index in range(7):
    new_turtle.make_turtle()
    new_turtle.set_speed(0, index)
    new_turtle.set_color(index)
    new_turtle.start(index)
    new_turtle.obj_list[index].showturtle()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
is_race_on = True
while is_race_on:
    for turtle in new_turtle.obj_list:
        if turtle.xcor() > 330:
            is_race_on = False
            winning_color = turtle.pencolor()
        rand_distance = random.randint(5, 30)
        turtle.forward(rand_distance)

if winning_color == user_bet:
    easygui.msgbox(f"You've won! The {winning_color} turtle is the winner!", title="Result")
else:
    easygui.msgbox(f"You've lost. The {winning_color} turtle is the winner!", title="Result")


screen.exitonclick()
