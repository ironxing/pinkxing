import turtle

little_turtle = turtle.Turtle()
little_turtle.color("red")

little_turtle.begin_fill()

for i in range(2):
    little_turtle.forward(30)
    little_turtle.left(90)
    little_turtle.forward(90)
    little_turtle.left(90)

little_turtle.end_fill()

little_turtle.penup()
little_turtle.goto(30,-80)
little_turtle.pendown()

little_turtle.color("black")
little_turtle.begin_fill()

for i in range(2):
    little_turtle.forward(100)
    little_turtle.left(90)
    little_turtle.forward(170)
    little_turtle.left(90)

little_turtle.end_fill()





turtle.done()