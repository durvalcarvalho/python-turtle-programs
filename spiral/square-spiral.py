import turtle

def draw_square(turtle, j, angle):
    for i in range(4):
        turtle.forward(j*2)
        turtle.right(angle)

def draw():
    # Turtle
    tur = turtle.Turtle()
    colors = ['red', 'blue', 'orange', 'violet', 'green', 'purple']

    col_t = 1
    rep = 50

    # Pen
    pen = turtle.Turtle()
    pen.speed("fastest")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(-290, 260)

    for angle in range(359, 0, -5):
        
        pen.clear()
        pen.write("Angle: {}".format(angle), align='center', font=("Counter", 10, "normal"))
        
        tur.speed("fastest")
        tur.pensize(1)
        tur.hideturtle()
        tur.color("yellow")

        for i in range(rep):

            draw_square(tur, i, angle)
            tur.right(angle-angle//2)

            if( i > (rep*col_t)//len(colors)):
                tur.color(colors[col_t])
                col_t += 1

                if(col_t-1 == len(colors)):
                    break
        
        tur.reset()
    
win = turtle.Screen()
win.bgcolor("black")
draw()
win.exitonclick()