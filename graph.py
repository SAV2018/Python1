# coding: utf-8
import turtle
import random
import math
import robot

def draw_circle_in(X, Y, radius, color):
    gotoXY(X, Y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def gotoXY(X, Y):
    turtle.penup()
    turtle.goto(X, Y)
    turtle.pendown()

def draw_circle(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_gun(start):
    # draw circles
    for i in range(start, random.randrange(7,50)):
        fi_rad = FI * i * math.pi / 180.0
        gotoXY(math.sin(fi_rad) * R, math.cos(fi_rad) * R + 60)
        draw_circle(22, 'brown')
        draw_circle(22, 'white')
    return i

FI = 360 / 7
R = 50

turtle.speed(0)

gotoXY(0,0)
turtle.circle(80)
gotoXY(0,160)
turtle.color('red')
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

answer = ''
start = 0
while answer != 'N':
    i = draw_gun(start)

    # fill one circle
    draw_circle(22, 'brown')

    # check result
    start = i % 7
    gotoXY(-50, 250)
    if i % 7 == 0:
        s = 'You lose!'
    else:
        s = 'You win!'

    turtle.write(s, font=('Arial', 18, 'normal'))
    answer = turtle.textinput('Continue?', 'Y/N')
    turtle.undo()

quit(0)

answer = ''
while answer != 'N':
    answer = turtle.textinput('Draw circle?', 'Y/N')
    if answer == 'Y':
        pass
    else:
        # draw random circle
        draw_circle_in(random.randrange(-300, 300), random.randrange(-200, 200), random.randrange(1, 100), [random.random(), random.random(), random.random()])

