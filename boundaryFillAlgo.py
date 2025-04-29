# # boundaryfill pseudocode
# boundary_fill(x,y,boundary_color,fill_color)
# {
#     int color;
#     getpixel(x,y);
#     if(color != boundary_color || color != fill_color)
#     {
#         setpixel(x,y,fill_color);
#         boundary_fill(x+1,y,boundary_color,fil_color);
#         boundary_fill(x,y+1,boundary_color,fil_color);
#         boundary_fill(x-1,y,boundary_color,fil_color);
#         boundary_fill(x,y-1,boundary_color,fil_color);
#     }
# }
import turtle
import math

def boundary_fill(x, y, boundary_color, fill_color, radius, center_x, center_y, screen):
    # Get the current position's "color" by checking if it's inside the circle
    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    
    # Check if the point is within the screen boundaries
    if not (-320 <= x <= 320 and -240 <= y <= 240):
        return
    
    # Simulate pixel color: inside circle but not on boundary
    if distance > radius + 1:  # Outside circle
        return
    if abs(distance - radius) <= 1:  # On boundary (approximately)
        return
    
    # If point hasn't been filled and isn't boundary
    if (x, y) not in filled_points:
        # Mark as filled
        filled_points.add((x, y))
        
        # Move turtle to position and draw a small dot
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot(2, fill_color)  # Small dot to simulate pixel
        
        # Recursively fill in four directions
        boundary_fill(x + 1, y, boundary_color, fill_color, radius, center_x, center_y, screen)
        boundary_fill(x - 1, y, boundary_color, fill_color, radius, center_x, center_y, screen)
        boundary_fill(x, y + 1, boundary_color, fill_color, radius, center_x, center_y, screen)
        boundary_fill(x, y - 1, boundary_color, fill_color, radius, center_x, center_y, screen)

def draw_circle(center_x, center_y, radius, color):
    turtle.penup()
    turtle.goto(center_x, center_y - radius)  # Start at bottom of circle
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)
    turtle.penup()

def main():
    global filled_points
    filled_points = set()  # To track filled points
    
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(640, 480)
    screen.bgcolor("black")
    
    # Initialize turtle
    turtle.speed(0)  # Fastest speed
    turtle.hideturtle()
    
    # Draw circle (center at (150, 200), radius 90)
    # Adjust y-coordinate: Turtle's (0,0) is center, so shift y by -240 to match OpenGL's bottom-left origin
    center_x, center_y = 150, 200 - 240
    radius = 90
    draw_circle(center_x, center_y, radius, "green")
    
    # Perform boundary fill starting at (150, 180 - 240)
    boundary_color = "green"
    fill_color = "blue"
    boundary_fill(150, 180 - 240, boundary_color, fill_color, radius, center_x, center_y, screen)
    
    # Keep window open until clicked
    screen.exitonclick()

if __name__ == "__main__":
    main()
