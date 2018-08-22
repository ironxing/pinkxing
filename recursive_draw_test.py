import turtle
import math

myTurtle = turtle.Turtle()
myTurtle.speed(10)


def square(r):
    for i in range(1, 5):
        myTurtle.forward(r)
        myTurtle.right(90)


def wow(a, r):
    while r>0:
        myTurtle.left(a)
        myTurtle.circle(math.sin(r))
        wow(a, r-1)

def fib(n):
    for n in range(400):
        turtle.color("black")
        turtle.right(3.1415*18)
        turtle.forward(n)
        if n > 400:
            break

fib(100)

turtle.done()