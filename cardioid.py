import turtle
import math

radius = 200
num = 200
jump = 1

# Window Setup
wn = turtle.Screen()
wn.title("Cardioid")

# Pen (Writing)
pen = turtle.Turtle()
pen.speed("fastest")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(-radius-80, radius+60)
pen.write("Times Table: {}".format(jump), align='center', font=("Counter", 10, "normal"))

# Turtle (Drawing)
tur = turtle.Turtle()
tur.speed("fastest")
turtle.Screen().bgcolor("white")

# Draw the circle

tur.up()
tur.goto(0, 0-radius)
tur.down()

tur.circle(radius)
tur.up()

# Go to center and point to bottom
tur.goto(0, 0)
tur.right(90)


def new_draw(tur):
    tur.reset()
    tur.speed("fastest")
    tur.up()
    tur.goto(0, 0-radius)
    tur.down()
    tur.circle(radius)
    tur.right(90)
    return tur

def select_color(tur, i):
    colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange', 'black']
    if(i%num < num * 1/7):
        tur.pencolor(colors[1])
    
    elif(i%num < num * 2/7):
        tur.pencolor(colors[2])

    elif(i%num < num * 3/7):
        tur.pencolor(colors[3])
    
    elif(i%num < num * 4/7):
        tur.pencolor(colors[4])
    
    elif(i%num < num * 5/7):
        tur.pencolor(colors[5])
    
    elif(i%num < num * 6/7):
        tur.pencolor(colors[6])
    
    else:
        tur.pencolor(colors[0])

    return tur

# The first coord (0)
coords = [(-0.00,-radius)]
i = 0
while(True):

    # colorful turtle
    # select_color(tur, i)
    
    # Movinto to the dots arround the circle
    tur.up()
    tur.goto(0, 0)
    tur.left(360/num)
    tur.forward(radius)
    tur.down()

    # if i hadn't complete the circle yet save the coords
    if(i<num-1):
        coords.append(tur.pos())

    # Find the spot and draw a line
    else:
        tur.hideturtle()
        val = (jump * i) % num
        tur.goto(coords[val])

        # if i had already complte the circle, reset the draw and start again a new one
        if(i%num==0):
            tur = new_draw(tur)
            jump += 1
    
            pen.clear()
            pen.write("Times Table: {}".format(jump), align='center', font=("Counter", 10, "normal"))
    i+=1    