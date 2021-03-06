#Pong in Python 3

import turtle
import time 
import os

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

# Sound
'''path = os.getcwd()
sound = path + (blah)'''

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions

def a_up():
    y = paddle_a.ycor()
    y += 20 
    paddle_a.sety(y)

def a_down():
    y = paddle_a.ycor()
    y -= 20 
    paddle_a.sety(y)

def b_up():
    y = paddle_b.ycor()
    y += 20 
    paddle_b.sety(y)

def b_down():
    y = paddle_b.ycor()
    y -= 20 
    paddle_b.sety(y)

# Keyboard binding
win.listen()
win.onkey(a_up, "w")
win.onkey(a_down, "s")
win.onkey(b_up, "Up")
win.onkey(b_down, "Down")


#main game loop
while True:
    time.sleep(.01)
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # boarder checking
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy*= -1
        os.system("afplay /Users/jonathanchin/Pong/bounce.wav&")
       
    
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy*= -1
        os.system("afplay /Users/jonathanchin/Pong/bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor()+50) and (ball.ycor() > paddle_b.ycor()-50):
        ball.dx *= -1
        os.system("afplay /Users/jonathanchin/Pong/bounce.wav&")

    if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor()+50) and (ball.ycor() > paddle_a.ycor()-50):
        ball.dx *= -1
        os.system("afplay /Users/jonathanchin/Pong/bounce.wav&")