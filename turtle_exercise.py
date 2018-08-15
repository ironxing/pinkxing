import turtle
little_turtle = turtle.Turtle()
little_turtle.speed(10)

little_turtle.color("red", "yellow")
little_turtle.begin_fill()

for i in range(36):
    little_turtle.forward(200)
    little_turtle.left(170)

little_turtle.end_fill()


turtle.done()