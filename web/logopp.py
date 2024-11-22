import turtle as t

def draw_rectangle(color, width, height, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_circle(color, radius, position):
    t.penup()
    t.goto(position[0], position[1] - radius)
    t.pendown()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(radius)
    t.end_fill()

# Setup layar
t.setup(600, 600)
t.speed(5)
t.bgcolor("white")

draw_circle("black", 100, (0, 0))

draw_circle("white", 90, (0, 0))


draw_circle("blue", 80, (0, 0))

draw_rectangle("red", 60, 40, (-30, -80))


t.penup()
t.goto(-30, -40)
t.pendown()
t.begin_fill()
t.fillcolor("red")
t.setheading(135)
t.circle(20, 180)  
t.setheading(0)
t.goto(-30, -40)  
t.end_fill()

draw_rectangle("red", 20, 90, (-30, -40))

draw_rectangle("red", 20, 60, (-10, -40))

draw_rectangle("red", 20, 60, (10, -40))

draw_rectangle("red", 20, 40, (30, -40))

draw_circle("black", 10, (-20, 50))

t.penup()
t.goto(0, -200)
t.color("black")
t.write("SMK PRESTASI PRIMA", align="center", font=("Arial", 16, "bold"))
t.goto(0, -230)
t.write("IF BETTER IS POSSIBLE, GOOD IS NOT ENOUGH", align="center", font=("Arial", 10, "italic"))

t.hideturtle()
t.done()