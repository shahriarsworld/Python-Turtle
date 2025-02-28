import turtle

def draw_circle(xc, yc, r):
    """Simple Bresenham's Circle Drawing Algorithm"""
    turtle.speed(0)
    turtle.penup()

    x, y = 0, r
    p = 1 - r  # Initial decision parameter

    def plot_points(x, y):
        """Plot the 8 symmetric points"""
        for px, py in [(x, y), (-x, y), (x, -y), (-x, -y),
                       (y, x), (-y, x), (y, -x), (-y, -x)]:
            turtle.goto(xc + px, yc + py)
            turtle.pendown()
            turtle.dot()  # Draw a point
            turtle.penup()

    plot_points(x, y)  # Plot initial points

    while x < y:
        x += 1
        if p < 0:  # Choose right pixel
            p += 2 * x + 1
        else:  # Choose diagonal pixel
            y -= 1
            p += 2 * (x - y) + 1

        plot_points(x, y)  # Plot new points

    turtle.done()

# Example: Draw a circle with center (0, 0) and radius 50
draw_circle(0, 0, 50)
