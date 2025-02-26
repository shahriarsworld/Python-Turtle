import turtle

t = turtle.Turtle()

t.color("red")
t.speed(2)

#square draw

for _ in range(4):
    t.forward(100)
    t.right(90)

#triangle draw
for _ in range(3):
    t.forward(150)
    t.right(120)

#pentagon draw
for _ in range(5):
    t.forward(150)
    t.right(72)

turtle.done()