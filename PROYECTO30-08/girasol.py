import turtle

# Configurar la ventana y el lápiz
ventana = turtle.Screen()
ventana.bgcolor("white")
lapiz = turtle.Turtle()
lapiz.speed(0)
lapiz.pensize(3)

# Dibujar la rama del girasol
lapiz.penup()
lapiz.goto(0, -200)
lapiz.pendown()
lapiz.color("brown")
lapiz.left(90)
lapiz.forward(200)

# Dibujar el centro del girasol
lapiz.color("black", "darkgoldenrod")
lapiz.begin_fill()
lapiz.circle(50)
lapiz.end_fill()

# Dibujar los pétalos del girasol
for i in range(24):
    lapiz.penup()
    lapiz.goto(0, 0)
    lapiz.left(15)
    lapiz.forward(50)
    lapiz.pendown()
    lapiz.color("black", "gold")
    lapiz.begin_fill()
    lapiz.circle(80, 60)
    lapiz.left(120)
    lapiz.circle(80, 60)
    lapiz.end_fill()

# Ocultar el lápiz y mantener la ventana abierta
lapiz.hideturtle()
ventana.mainloop()
