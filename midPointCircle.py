import turtle

# Input: Get circle center (xc, yc) and radius (r)
xc = int(input("Enter Center X: "))
yc = int(input("Enter Center Y: "))
r = int(input("Enter Radius: "))

def draw_circle_midpoint(xc, yc, r):

    turtle.speed(0)  # Fastest drawing speed
    turtle.penup()

    # Initialize values as per the pseudocode
    x = 0
    y = r
    p = 1 - r  # Initial decision parameter

    while x <= y:
        # Plot 8 symmetric points
        for dx, dy in [(x, y), (y, x), (-y, x), (-x, y),
                       (-x, -y), (-y, -x), (y, -x), (x, -y)]:
            turtle.goto(xc + dx, yc + dy)
            turtle.pendown()
            turtle.dot()
            turtle.penup()

        # Midpoint algorithm update (following the given pseudocode)
        if p < 0:
            p = p + (2 * x) + 3
        else:
            p = p + (2 * (x - y)) + 6
            y -= 1
        x += 1

    # Finish Turtle
    turtle.done()

# Call function to draw circle
draw_circle_midpoint(xc, yc, r)
