import turtle

def draw(sides,length):
    t = turtle.Turtle()
    t.color("blue")
    t.speed(4)

    for _ in range(sides):
        t.forward(length)
        t.left(360/sides)
 
    turtle.done()

def star(points,length):
    t = turtle.Turtle()
    t.color("blue")
    t.speed(4)
    for _ in range(points):
          t.forward(length)
          t.right(144)
    turtle.done()


star(5,150)