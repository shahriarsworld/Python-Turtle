import turtle

t = turtle.Turtle()

t.color("blue")
t.speed(1)
t.shape("turtle")

for _ in range(100):
    t.forward(10)
    t.left(10)

turtle.done()
