import turtle
little_turtle = turtle.Turtle()
little_turtle.speed(10)

def flower(color1, color2):
    little_turtle.color(color1, color2)
    little_turtle.begin_fill()

    for i in range(36):
        little_turtle.forward(200)
        little_turtle.left(170)

    little_turtle.end_fill()


little_turtle.color("red", "yellow")
little_turtle.begin_fill()

for i in range(36):
    little_turtle.forward(200)
    little_turtle.left(170)

little_turtle.end_fill()

little_turtle.penup()
little_turtle.left(5)
little_turtle.forward(60)
little_turtle.pendown()

little_turtle.color("red", "white")
little_turtle.begin_fill()

for i in range(36):
    little_turtle.forward(80)
    little_turtle.left(170)

little_turtle.end_fill()


turtle.done()