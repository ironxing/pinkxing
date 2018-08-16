import turtle

turtle.speed(10)

def flower(color1, color2, iteration):
    turtle.color(color1, color2)
    turtle.begin_fill()

    for i in range(iteration):
        turtle.forward(d)
        turtle.left(angle)

    turtle.end_fill()

flower("red", "yellow", 36, d, angle)