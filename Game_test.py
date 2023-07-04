import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Spaceship Game")

spaceship = turtle.Turtle()
spaceship.color("black")
spaceship.shape('circle')
spaceship.penup()

speed = 0
dead = False

def up():
    if spaceship.heading() != 90:
        spaceship.setheading(90)

def down():
    if spaceship.heading() != 270:
        spaceship.setheading(270)  

def left():
    if spaceship.heading() != 180:
        spaceship.setheading(180)

def right():
    if spaceship.heading() != 0:
        spaceship.setheading(0)

def space_bar():
    global speed
    if speed == 0:
        speed = 1
    else:
        speed = 0

def check_boundary():
    x, y = spaceship.position()
    if x < -400 or x > 400 or y < -400 or y > 400:
        spaceship.color("red")
        wn.bgcolor("black")
        global dead
        dead = True

wn.listen()
wn.onkey(up, 'Up')
wn.onkey(down, 'Down')
wn.onkey(left, 'Left')
wn.onkey(right, 'Right')
wn.onkey(space_bar, 'space')

while True:
    spaceship.forward(speed)
    check_boundary()

    if speed == 1:
        spaceship.speed(10)
        wn.bgcolor("yellow")
    elif speed == 0:
        spaceship.speed(0)
        wn.bgcolor("light green")

    if dead:
        break

wn.mainloop()
