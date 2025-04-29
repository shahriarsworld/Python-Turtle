# Koch Curve

# pseudocode:

#  n= 0
# koch_curve(x,y,len,alpha,n)
# {
# len= len/3;
# koch_curve(x,y,len,alpha, n-1);
# x= len*cos(alpha);
# y= len*sin(alpha);
# koch_curve(x,y,len,alpha-60,n-1);
# x= len*cos(alpha-60);
# y= len*sin(alpha-60);
# koch_curve(x,y,len,alpha+60,n-1);
# x= len*cos(alpha+60);
# y=len*sin(alpha+60);
# koch_curve(x,y,len,alpha,n-1);
# }
# else
# drawline(x,y,x+len*cos(alpha), y+len*sin(alpha));
# }

import turtle
import math

def koch_curve(x, y, length, alpha, n):
    if n == 0:

        x_end = x + length * math.cos(math.radians(alpha))
        y_end = y + length * math.sin(math.radians(alpha))
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x_end, y_end)
    else:

        length = length / 3

        koch_curve(x, y, length, alpha, n-1)
        x = x + length * math.cos(math.radians(alpha))
        y = y + length * math.sin(math.radians(alpha))

        koch_curve(x, y, length, alpha - 60, n-1)
        x = x + length * math.cos(math.radians(alpha - 60))
        y = y + length * math.sin(math.radians(alpha - 60))

        koch_curve(x, y, length, alpha + 60, n-1)
        x = x + length * math.cos(math.radians(alpha + 60))
        y = y + length * math.sin(math.radians(alpha + 60))

        koch_curve(x, y, length, alpha, n-1)

turtle.speed(0)
turtle.hideturtle()

start_x = -200
start_y = 0
length = 400
alpha = 0
depth = 3

koch_curve(start_x, start_y, length, alpha, depth)

turtle.done()
