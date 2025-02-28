import turtle  

def draw_line_DDA(x1, y1, x2, y2):
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed

    # Step 1: Calculate ΔX and ΔY
    dx = x2 - x1
    dy = y2 - y1

    # Step 2: Find the number of steps
    steps = max(abs(dx), abs(dy))

    # Step 3: Calculate increments
    x_inc = dx / steps
    y_inc = dy / steps

    # Step 4: Start drawing
    x, y = x1, y1
    for _ in range(steps):
        t.goto(round(x), round(y))  # Move to nearest pixel
        x += x_inc
        y += y_inc

    turtle.done()

# Call function with start and end points
draw_line_DDA(-100, -100, 100, 50)
