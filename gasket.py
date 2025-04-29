# # gasket(x1,y1,x2,y2,x3,y3,n)
# {
#     if(n>0)
#     {
#         x12 = (x1+x2)/2
#         x13 = (x1+x3)/2
#         x23 = (x2+x3)/2
#         y12 = (y1+y2)/2
#         y13 = (y1+y3)/2
#         y23 = (y2+y3)/2
#     }
#     gasket(x1,y1,x12,y12,x13,y13);
#     gasket(x2,y2,x23,y23,x12,y12);
#     gasket(x3,y3,x13,y13,x23,y23);
# }
# else{
#     drawtriangle(x1,y1,x2,y2,x3,y3)
# }
# }

import turtle

def draw_triangle(x1, y1, x2, y2, x3, y3):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)

def gasket(x1, y1, x2, y2, x3, y3, n):
    if n == 0:

        draw_triangle(x1, y1, x2, y2, x3, y3)
    else:
        x12 = (x1 + x2) / 2
        y12 = (y1 + y2) / 2

        x13 = (x1 + x3) / 2
        y13 = (y1 + y3) / 2

        x23 = (x2 + x3) / 2
        y23 = (y2 + y3) / 2

        # Recursively draw three smaller triangles
        gasket(x1, y1, x12, y12, x13, y13, n-1)
        gasket(x2, y2, x23, y23, x12, y12, n-1)
        gasket(x3, y3, x13, y13, x23, y23, n-1)


turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")

x1, y1 = -200, -100
x2, y2 = 0, 200
x3, y3 = 200, -100
depth = 3 


gasket(x1, y1, x2, y2, x3, y3, depth)


turtle.done()
