import turtle

def bresenham_line(x1, y1, x2, y2):
    turtle.penup()  
    turtle.goto(x1 * 10, y1 * 10)  # Scale up for visibility
    turtle.pendown()  
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    p = 2 * dy - dx
    
    x, y = x1, y1
    
    while x != x2 or y != y2:
        turtle.goto(x * 10, y * 10)  # Scale coordinates for better visibility
        if p >= 0:
            y += sy
            p -= 2 * dx
        x += sx
        p += 2 * dy

    turtle.goto(x2 * 10, y2 * 10)  # Draw final point
    turtle.done()

# Example usage
bresenham_line(2,2,8,5)
