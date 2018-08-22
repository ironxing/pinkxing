import turtle

betty = turtle.Turtle()
betty.speed(10)


def circle_get_smaller(n):
    if n == 1:
        betty.circle(50)
    else:
        betty.circle(2*circle_get_smaller(n-1))

def number_get_smaller(n):
    if n == 1:
        a = 100
    else:
        a = 0.8 * (n-1)

a = number_get_smaller(100)
print(a)


circle_get_smaller(100)
turtle.done()

