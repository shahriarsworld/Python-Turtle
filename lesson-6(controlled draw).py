import turtle

# Setup
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

# Function to move turtle to mouse click position
def go_to_click(x, y):
    t.penup()  # Lift the pen to avoid drawing lines
    t.goto(x, y)  # Move turtle to the clicked position
    t.pendown()  # Put the pen back down to start drawing

# Set the screen click event
turtle.onscreenclick(go_to_click)  # Detects mouse clicks on the screen

# Keep the screen open
turtle.done()
