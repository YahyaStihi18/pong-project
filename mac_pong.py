# pong game
# Author "Yahya Stihi" email: stihiyahya2016@gmail.com
# player A plays with "A" and "Q" player B plays with "Up" and "Down" you can change it in line 96 to 99
# Note: this is the mac version "works only on mac os"
# you can change the speed from line 49, 50 and they must be equal

import os
import turtle

wn = turtle.Screen()
wn.title("PONG BY YAHYA")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# score
score_a = 0
score_b = 0


# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-390, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(380, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)

# === you can change the speed from her, put any number above 0 ===
ball.dx = 0.2
ball.dy = 0.2
# =================================================================


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(0, 270)
pen.write("player A: 0 =VS= player B: 0", align="center", font=("courier", 20, "normal"))


# functions


# for paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)
# for paddle B


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)

# keyboard binding
# ===you can change the buttons to whatever you want to play with===

wn.listen()
wn.onkeypress(paddle_a_up, "a")
wn.onkeypress(paddle_a_down, "q")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# ===================================================================

# main game loop
while True:

    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"player A: {score_a} =VS= player B: {score_b}", align="center", font=("courier", 20, "normal"))
        os.system("afplay win.wav&")
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"player A: {score_a} =VS= player B: {score_b}", align="center", font=("courier", 20, "normal"))
        os.system("afplay win.wav&")
        
    # paddle hits ball
    if (ball.xcor() > 360 and ball.xcor() < 370 ) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40 ):
        ball.setx(360)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    if (ball.xcor() < -370 and ball.xcor()> -380) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor()-40 ):
        ball.setx(-370)
        ball.dx *= -1
        os.system("afplay bounce.wav&")