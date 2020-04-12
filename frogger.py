import turtle
import random

wn = turtle.Screen()
wn.title("frogger")
wn.bgcolor("black")
wn.setup(width=1200, height=600)
wn.tracer(0)

at_menu = True

#score
score = 0
lives = 3
random_side = [-1, 1]

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

"""# title pen
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
exit_pen.write("Exit", align="center", font=("Courier", 24, "normal"))"""

# score pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(-200, 260)
score_pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# lives pen
lives_pen = turtle.Turtle()
lives_pen.speed(0)
lives_pen.color("white")
lives_pen.penup()
lives_pen.hideturtle()
lives_pen.goto(200, 260)
lives_pen.write("lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))

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
car_1 = Car("car1", "pictures/car1.gif", "pictures/car1.2.gif", 1.5, -150, 62)
car_1.set_car()

# car 2
car_2 = Car("car2", "pictures/car2.gif", "pictures/car2.2.gif", 1, -100, 50)
car_2.set_car()

# car 3
car_3 = Car("car3", "pictures/car3.gif", "pictures/car3.2.gif", 2, -50, 58)
car_3.set_car()

# car 4
car_4 = Car("car4", "pictures/car4.gif", "pictures/car4.2.gif", 1.3, 0, 77)
car_4.set_car()

# car 5
car_5 = Car("car5", "pictures/bus1.gif", "pictures/bus1.2.gif", 1.4, 50, 102)
car_5.set_car()

# car 6
car_6 = Car("car6", "pictures/truck1.gif", "pictures/truck1.2.gif", 1.7, 100, 85)
car_6.set_car()

# car 7
car_7 = Car("car7", "pictures/car5.gif", "pictures/car5.2.gif", 1.6, 150, 69)
car_7.set_car()

# car 8
car_8 = Car("car8", "pictures/bus2.gif", "pictures/bus2.2.gif", 1.2, 200, 87)
car_8.set_car()

# function
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

"""def menu_up():
    start_pen.clear()
    start_pen.color("light green")
    start_pen.write("Start", align="center", font=("Courier", 24, "bold"))

    exit_pen.clear()
    exit_pen.color("white")
    exit_pen.write("Exit", align="center", font=("Courier", 24, "normal"))

def menu_down():
    exit_pen.clear()
    exit_pen.color("light green")
    exit_pen.write("Exit", align="center", font=("Courier", 24, "bold"))

    start_pen.clear()
    start_pen.color("white")
    start_pen.write("Start", align="center", font=("Courier", 24, "normal"))

def exit_menu():
    title_pen.hideturtle()
    start_pen.hideturtle()
    exit_pen.hideturtle()
    frog.showturtle()
    car_1.showturtle()
    wn.bgpic("pictures/road.gif")
    return False"""

# keyboard binding
wn.listen()
wn.onkey(frog_up, "w")

# main game loop
while True:
    wn.update()

    """while at_menu:
        wn.update()
        wn.onkey(menu_up, "Up")
        wn.onkey(menu_down, "Down")
        if wn.onkey(exit_menu, "space"):
            at_menu = False
            exit_menu()"""

    # !! remove when menu is working !!
    frog.showturtle()
    car_1.name.showturtle()
    wn.bgpic("pictures/road.gif")

    # score
    if frog.ycor() > 250:
        frog.goto(0, -300)
        score += 1
        score_pen.clear()
        score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # move car 1
    car_1.name.showturtle()
    car_1.name.setx(car_1.name.xcor() + car_1.name.dx)

    if car_1.name.xcor() < -650 or car_1.name.xcor() > 650:
        side = random.choice(random_side)
        car_1.name.setx(650 * side)
        car_1.name.dx *= -1
        if car_1.name.dx > 0:
            car_1.name.shape(car_1.rightward)
        else:
            car_1.name.shape(car_1.leftward)
        if score > 7:
            change_speed(car_1.name)

    # display and move car 2
    if score > 0:
        car_2.name.showturtle()
        car_2.name.setx(car_2.name.xcor() + car_2.name.dx)

        if car_2.name.xcor() < -650 or car_2.name.xcor() > 650:
            side = random.choice(random_side)
            car_2.name.setx(650 * side)
            car_2.name.dx *= -1
            if car_2.name.dx > 0:
                car_2.name.shape(car_2.rightward)
            else:
                car_2.name.shape(car_2.leftward)
            if score > 7:
                change_speed(car_2.name)

    # display and move car 3
    if score > 1:
        car_3.name.showturtle()
        car_3.name.setx(car_3.name.xcor() + car_3.name.dx)

        if car_3.name.xcor() < -650 or car_3.name.xcor() > 650:
            side = random.choice(random_side)
            car_3.name.setx(650 * side)
            car_3.name.dx *= -1
            if car_3.name.dx > 0:
                car_3.name.shape(car_3.rightward)
            else:
                car_3.name.shape(car_3.leftward)
            if score > 7:
                change_speed(car_3.name)

    # display and move car 4
    if score > 2:
        car_4.name.showturtle()
        car_4.name.setx(car_4.name.xcor() + car_4.name.dx)

        if car_4.name.xcor() < -650 or car_4.name.xcor() > 650:
            side = random.choice(random_side)
            car_4.name.setx(650 * side)
            car_4.name.dx *= -1
            if car_4.name.dx > 0:
                car_4.name.shape(car_4.rightward)
            else:
                car_4.name.shape(car_4.leftward)
            if score > 7:
                change_speed(car_4.name)

    # display and move car 5
    if score > 3:
        car_5.name.showturtle()
        car_5.name.setx(car_5.name.xcor() + car_5.name.dx)

        if car_5.name.xcor() < -650 or car_5.name.xcor() > 650:
            side = random.choice(random_side)
            car_5.name.setx(650 * side)
            car_5.name.dx *= -1
            if car_5.name.dx > 0:
                car_5.name.shape(car_5.rightward)
            else:
                car_5.name.shape(car_5.leftward)
            if score > 7:
                change_speed(car_5.name)

    # display and move car 6
    if score > 4:
        car_6.name.showturtle()
        car_6.name.setx(car_6.name.xcor() + car_6.name.dx)

        if car_6.name.xcor() < -650 or car_6.name.xcor() > 650:
            side = random.choice(random_side)
            car_6.name.setx(650 * side)
            car_6.name.dx *= -1
            if car_6.name.dx > 0:
                car_6.name.shape(car_6.rightward)
            else:
                car_6.name.shape(car_6.leftward)
            if score > 7:
                change_speed(car_6.name)

    # display and move car 7
    if score > 5:
        car_7.name.showturtle()
        car_7.name.setx(car_7.name.xcor() + car_7.name.dx)

        if car_7.name.xcor() < -650 or car_7.name.xcor() > 650:
            side = random.choice(random_side)
            car_7.name.setx(650 * side)
            car_7.name.dx *= -1
            if car_7.name.dx > 0:
                car_7.name.shape(car_7.rightward)
            else:
                car_7.name.shape(car_7.leftward)
            if score > 7:
                change_speed(car_7.name)

    # display and move car 8
    if score > 6:
        car_8.name.showturtle()
        car_8.name.setx(car_8.name.xcor() + car_8.name.dx)

        if car_8.name.xcor() < -650 or car_8.name.xcor() > 650:
            side = random.choice(random_side)
            car_8.name.setx(650 * side)
            car_8.name.dx *= -1
            if car_8.name.dx > 0:
                car_8.name.shape(car_8.rightward)
            else:
                car_8.name.shape(car_8.leftward)
            if score > 7:
                change_speed(car_8.name)

    # hit detection
    cars = [car_1, car_2, car_3, car_4, car_5, car_6, car_7, car_8]

    for i in cars:
        if frog.xcor() > i.name.xcor() - i.hitbox and frog.xcor() < i.name.xcor() + i.hitbox and frog.ycor() < i.name.ycor() + 35 and frog.ycor() > i.name.ycor() - 45:
            lives = lose_life(lives)
