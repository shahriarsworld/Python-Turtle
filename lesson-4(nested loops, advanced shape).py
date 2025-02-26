import turtle

t = turtle. Turtle()
t.color("red")
t.shape("turtle")
t.speed(7)

for _ in range(8):
    for _ in range(5):
        t.forward(100)
        t.left(144)
        
    t.penup()
    t.right(45)
    t.forward(110)
    t.pendown()

turtle.done()