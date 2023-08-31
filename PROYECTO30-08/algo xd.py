import turtle

turtle.setup(800, 800)
turtle.speed(0)
turtle.tracer(10)
turtle.width(2)
turtle.bgcolor("black")
for i in range(25):
    for j in range(15):
        turtle.color("purple")
        turtle.right(90)
        turtle.circle(200-i*4, 90)
        turtle.left(90)
        turtle.circle(200-i*4, 90)
        turtle.right(180)
        turtle.circle(50, 24)

# Añadir tallo y hojas
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.color("green")
turtle.right(90)
turtle.forward(300)

# Añadir hojas
for i in range(2):
    turtle.right(45)
    turtle.circle(-50, 90)
    turtle.left(90)
    turtle.circle(-50, 90)

turtle.hideturtle()
turtle.done()

"""import colorsys as cs 
turtle.setup(800, 800)
turtle.speed(0)
turtle.tracer(10)
turtle.width(2)
turtle.bgcolor("black")
for i in range(25):
    for j in range(15):
        turtle.color(cs.hls_to_rgb(j/15,i/25, 1))
        turtle.right(90)
        turtle.circle(200-i*4, 90)
        turtle.left(90)
        turtle.circle(200-i*4, 90)
        turtle.right(180)
        turtle.circle(50, 24)
turtle.hideturtle()
turtle.done()"""