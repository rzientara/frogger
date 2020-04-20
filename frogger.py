import turtle
import random
import os

wn = turtle.Screen()
wn.title("frogger")
wn.bgcolor("black")
wn.setup(width=1200, height=600)
wn.tracer(0)

###################
# variables
###################
at_menu = True
play_game = True
quit_game = False
score = 0
lives = 3
random_side = [-1, 1]

# high score variables
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters_chosen = ["_", "_", "_"]
letter_amount = 0
letter_number = 0

###################
# turtles
###################

# frog
frog = turtle.Turtle()
frog.speed(0)
frog_shape = "pictures/frog.gif"
wn.addshape(frog_shape)
frog.shape(frog_shape)
frog.penup()
frog.shapesize(1.5)
frog.goto(0, -300)
frog.tilt(90)
frog.hideturtle()

# title pen
title_pen = turtle.Turtle()
title_pen.speed(0)
title_pen.color("white")
title_pen.penup()
title_pen.hideturtle()
title_pen.goto(0, 60)
title_pen.write("Welcome to Frogger", align="center", font=("Courier", 24, "normal"))

# start pen
start_pen = turtle.Turtle()
start_pen.speed(0)
start_pen.color("light green")
start_pen.penup()
start_pen.hideturtle()
start_pen.goto(0, 20)
start_pen.write("Start", align="center", font=("Courier", 24, "bold"))

# exit pen
exit_pen = turtle.Turtle()
exit_pen.speed(0)
exit_pen.color("white")
exit_pen.penup()
exit_pen.hideturtle()
exit_pen.goto(0, -20)
exit_pen.write("Exit", align="center", font=("Courier", 24, "normal"))

# name pen
name_pen = turtle.Turtle()
name_pen.speed(0)
name_pen.color("light green")
name_pen.penup()
name_pen.hideturtle()
name_pen.goto(0, 20)

# score pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(-200, 260)

# lives pen
lives_pen = turtle.Turtle()
lives_pen.speed(0)
lives_pen.color("white")
lives_pen.penup()
lives_pen.hideturtle()
lives_pen.goto(200, 260)

###################
# classes
###################
class Car:
    def __init__(self, name, rightward, leftward, speed, ypos, hitbox):
        self.name = name
        self.rightward = rightward
        self.leftward = leftward
        self.speed = speed
        self.ypos = ypos
        self.hitbox = hitbox

    def set_car(self):
        self.name = turtle.Turtle()
        self.name.speed(0)
        self.name.penup()
        wn.addshape(self.rightward)
        wn.addshape(self.leftward)
        self.name.shape(self.rightward)
        self.name.shapesize(stretch_wid=2, stretch_len=4)
        self.name.hideturtle()
        self.name.goto(650, self.ypos)
        self.name.dx = self.speed

# car 1
car_1 = Car("car1", "pictures/car1.gif", "pictures/car1.2.gif", .5, -150, 62)
car_1.set_car()

# car 2
car_2 = Car("car2", "pictures/car2.gif", "pictures/car2.2.gif", .3, -100, 50)
car_2.set_car()

# car 3
car_3 = Car("car3", "pictures/car3.gif", "pictures/car3.2.gif", .7, -50, 58)
car_3.set_car()

# car 4
car_4 = Car("car4", "pictures/car4.gif", "pictures/car4.2.gif", .45, 0, 77)
car_4.set_car()

# car 5
car_5 = Car("car5", "pictures/bus1.gif", "pictures/bus1.2.gif", .35, 50, 102)
car_5.set_car()

# car 6
car_6 = Car("car6", "pictures/truck1.gif", "pictures/truck1.2.gif", .4, 100, 85)
car_6.set_car()

# car 7
car_7 = Car("car7", "pictures/car5.gif", "pictures/car5.2.gif", .55, 150, 69)
car_7.set_car()

# car 8
car_8 = Car("car8", "pictures/bus2.gif", "pictures/bus2.2.gif", .6, 200, 87)
car_8.set_car()

cars = [car_1, car_2, car_3, car_4, car_5, car_6, car_7, car_8]

###################
# functions
###################
def frog_up():
    y = frog.ycor()
    y += 50
    frog.sety(y)

def lose_life(lives):
    frog.sety(-300)
    lives -= 1
    lives_pen.clear()
    lives_pen.write("lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
    return lives

def change_speed(car):
    if car.dx > 0:
        car.dx = random.uniform(1, 2)
    else:
        car.dx = random.uniform(-1, -2)

def menu_up():
    global play_game
    global quit_game

    # select top option
    start_pen.clear()
    start_pen.color("light green")
    start_pen.write("Start", align="center", font=("Courier", 24, "bold"))
    play_game = True

    # deselect bottom option
    exit_pen.clear()
    exit_pen.color("white")
    exit_pen.write("Exit", align="center", font=("Courier", 24, "normal"))
    quit_game = False

def menu_down():
    global play_game
    global quit_game

    # select bottom option
    exit_pen.clear()
    exit_pen.color("light green")
    exit_pen.write("Exit", align="center", font=("Courier", 24, "bold"))
    quit_game = True

    # deselect bottom option
    start_pen.clear()
    start_pen.color("white")
    start_pen.write("Start", align="center", font=("Courier", 24, "normal"))
    play_game = False

def exit_menu():
    if play_game:
        # display game and hide menu
        title_pen.clear()
        start_pen.clear()
        exit_pen.clear()
        frog.showturtle()
        car_1.name.showturtle()
        wn.bgpic("pictures/road.gif")
        score_pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        lives_pen.write("lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))

        # disable menu keys and enable frog key
        wn.onkey(None, "Up")
        wn.onkey(None, "Down")
        wn.onkey(None, "Space")
        wn.onkey(frog_up, "w")

        global  at_menu
        at_menu = False
    if quit_game:
        os._exit(0)

def open_menu():
    # display menu and hide game
    title_pen.write("Welcome to Frogger", align="center", font=("Courier", 24, "normal"))
    start_pen.write("Start", align="center", font=("Courier", 24, "bold"))
    exit_pen.write("Exit", align="center", font=("Courier", 24, "normal"))

    wn.onkey(menu_up, "w")
    wn.onkey(menu_down, "s")
    wn.onkey(exit_menu, "space")

    global at_menu
    at_menu = True

def letter_up():
    global letter_number

    if letter_number == 25:
        letter_number = 0
    else:
        letter_number += 1

def letter_down():
    global letter_number

    if letter_number == 0:
        letter_number = 25
    else:
        letter_number -= 1

def select_letter():
    global letter_amount
    global letter_number

    letter_amount += 1
    letter_number = 0

def move_car(car):
    car.name.setx(car.name.xcor() + car.name.dx)

def reset_car(car, random_side):
    if car.name.xcor() < -650 or car.name.xcor() > 650:
        side = random.choice(random_side)
        car.name.setx(650 * side)
        car.name.dx *= -1
        if car.name.dx > 0:
            car.name.shape(car.rightward)
        else:
            car.name.shape(car.leftward)
        if score > 7:
            change_speed(car.name)

def clear_game():
    wn.bgpic("nopic")
    wn.bgcolor("black")
    score_pen.clear()
    lives_pen.clear()
    frog.hideturtle()
    for i in cars:
        i.name.hideturtle()
        i.name.goto(650, i.ypos)

def close_high_score(number, amount, score, lives):
    letter_number = 0
    letter_amount = 0
    title_pen.clear()
    name_pen.clear()
    score = 0
    lives = 3
    return False

# start at menu
wn.listen()
open_menu()

###################
# main game loop
###################
while True:
    wn.update()

    while at_menu:
        wn.update()

    # score
    if frog.ycor() > 250:
        frog.goto(0, -300)
        score += 1
        score_pen.clear()
        score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # move car 1
    car_1.name.showturtle()
    move_car(car_1)
    reset_car(car_1, random_side)

    # display and move car 2
    if score > 0:
        car_2.name.showturtle()
        move_car(car_2)
        reset_car(car_2, random_side)

    # display and move car 3
    if score > 1:
        car_3.name.showturtle()
        move_car(car_3)
        reset_car(car_3, random_side)

    # display and move car 4
    if score > 2:
        car_4.name.showturtle()
        move_car(car_4)
        reset_car(car_4, random_side)

    # display and move car 5
    if score > 3:
        car_5.name.showturtle()
        move_car(car_5)
        reset_car(car_5, random_side)

    # display and move car 6
    if score > 4:
        car_6.name.showturtle()
        move_car(car_6)
        reset_car(car_6, random_side)

    # display and move car 7
    if score > 5:
        car_7.name.showturtle()
        move_car(car_7)
        reset_car(car_7, random_side)

    # display and move car 8
    if score > 6:
        car_8.name.showturtle()
        move_car(car_8)
        reset_car(car_8, random_side)

    # hit detection
    for i in cars:
        if i.name.xcor() - i.hitbox < frog.xcor() < i.name.xcor() + i.hitbox and i.name.ycor() + 35 > frog.ycor() > i.name.ycor() - 45:
            lives = lose_life(lives)

    # if out of lives, clear game screen
    if lives < 0:
        clear_game()

        # disable frog key
        wn.onkey(None, "w")

        # high score menu
        high_score_s = True
        while high_score_s:
            wn.update()
            if letter_amount < 3:
                # keys for name entry
                wn.onkey(letter_up, "w")
                wn.onkey(letter_down, "s")
                wn.onkey(select_letter, "space")

                letters_chosen[letter_amount] = letters[letter_number]
                title_pen.write("-New High Score-\n Enter name:", align="center", font=("Courier", 24, "normal"))
                name_pen.clear()
                name_pen.write("{}{}{}".format(letters_chosen[0], letters_chosen[1], letters_chosen[2]), align="center", font=("Courier", 24, "normal"))
            else:
                high_score_s = close_high_score(letter_number, letter_amount, score, lives)
        # reset score and lives
        open_menu()