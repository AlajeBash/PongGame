# Simple Pong Game in Python For Beginners
# Bashir Sani

# Part 1: Creating the play Ground 
# Part 2: Adding the two Paddles and Ball
# Part 3: Moving the Paddles
# Part 4: Moving the Ball
# Part 5: Colliding With the Paddles

import turtle as t

pg = t.Screen() #pg Stands for Play Ground which is the field
pg.title("Pong Game by Bashir Sani")
pg.bgcolor("black")
pg.setup(width=800, height=600)
pg.tracer(0)

# Paddle A
paddle_a = t.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("White")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = t.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("White")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("White")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Function
# Moving Paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Moving Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
# Keyboard Binding
pg.listen()
pg.onkeypress(paddle_a_up, "w")
pg.onkeypress(paddle_a_down, "s")
pg.onkeypress(paddle_b_up, "Up")
pg.onkeypress(paddle_b_down, "Down")
# Main Game loop
while True:
    pg.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    # Top Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # Bottom Border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # Left Border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    # Right Border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Colliding 
    # Left Paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx = -1

    # Right Paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx = -1