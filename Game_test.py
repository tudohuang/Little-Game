import turtle
import os
import random

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

# Create Enemy and its bullet
enemies = []
enemy_bullets = []
num_of_enemies = 10
for i in range(num_of_enemies):
    enemies.append(turtle.Turtle())
    enemies[i].color("red")
    enemies[i].shape("circle")
    enemies[i].penup()
    enemies[i].speed(0)
    enemies[i].setposition(-200 + i*40, 250)

    enemy_bullets.append(turtle.Turtle())
    enemy_bullets[i].color("green")
    enemy_bullets[i].shape("triangle")
    enemy_bullets[i].penup()
    enemy_bullets[i].speed(0)
    enemy_bullets[i].setheading(270)
    enemy_bullets[i].shapesize(0.5, 0.5)
    enemy_bullets[i].hideturtle()

enemyspeed = 2
enemybulletspeed = 10
enemybulletstate = ["ready"] * num_of_enemies

# Functions
def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def fire_enemy_bullet(i):
    global enemybulletstate
    if enemybulletstate[i] == "ready":
        enemybulletstate[i] = "fire"
        x = enemies[i].xcor()
        y = enemies[i].ycor() - 10
        enemy_bullets[i].setposition(x, y)
        enemy_bullets[i].showturtle()

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def is_collision(t1, t2):
    return t1.distance(t2) < 15

# Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Game Loop
while True:
    for i in range(num_of_enemies):
        x = enemies[i].xcor()
        x += enemyspeed
        enemies[i].setx(x)

        if enemies[i].xcor() > 280:
            for j in range(num_of_enemies):
                y = enemies[j].ycor()
                y -= 40
                enemies[j].sety(y)
            enemyspeed *= -1

        if enemies[i].xcor() < -280:
            for j in range(num_of_enemies):
                y = enemies[j].ycor()
                y -= 40
                enemies[j].sety(y)
            enemyspeed *= -1

        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

        if enemybulletstate[i] == "fire":
            y = enemy_bullets[i].ycor()
            y -= enemybulletspeed
            enemy_bullets[i].sety(y)

        if enemy_bullets[i].ycor() < -275:
            enemy_bullets[i].hideturtle()
            enemybulletstate[i] = "ready"

        if is_collision(bullet, enemies[i]):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            enemies[i].hideturtle()
            enemies[i].setposition(0, 1000)

        if is_collision(player, enemies[i]) or is_collision(player, enemy_bullets[i]):
            player.hideturtle()
            enemies[i].hideturtle()
            enemy_bullets[i].hideturtle()
            print("Game Over")
            break

        if random.randint(1, 100) == 1 and enemybulletstate[i] == "ready":
            fire_enemy_bullet(i)
