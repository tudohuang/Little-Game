import turtle
import os

win = turtle.Screen()
win.bgcolor("black")

# Create Player
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Create Enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

# Player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

bulletstate = "ready"

# Move Player
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -290:
        x = -290
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 290:
        x = 290
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def is_collision(t1, t2):
    distance = abs(t1.distance(t2))
    if distance < 15:
        return True
    else:
        return False

# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Game Loop
while True:
    # Move Enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    if enemy.xcor() > 290:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    if enemy.xcor() < -290:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    # Move Bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    if is_collision(bullet, enemy):
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        enemy.setposition(-200, 250)

    if is_collision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break
