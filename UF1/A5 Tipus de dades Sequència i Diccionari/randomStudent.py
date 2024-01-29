import random

CORREO = ("tamoor.asghar.7e7@itb.cat",
    "xavier.cabello.7e7@itb.cat",
    "oriol.canellas.7e3@itb.cat",
    "ayman.dghoughi.7e7@itb.cat",
    "ian.diaz.7e7@itb.cat",
    "nizar.elkhoulfi.7e7@itb.cat",
    "izan.fernandez.7e7@itb.cat",
    "eric.gonzalez.7e7@itb.cat",
    "hugo.gonzalez.7e7@itb.cat",
    "marc.guerra.7e7@itb.cat",
    "rafael.guiotto.7e7@itb.cat",
    "jaffet.hernandez.7e5@itb.cat",
    "daniel.hernandez.zerpa.7e7@itb.cat",
    "helena.herrera.7e5@itb.cat",
    "faizan.hussain.7e7@itb.cat",
    "iker.jimenez.7e7@itb.cat",
    "matvei.karikh.7e6@itb.cat",
    "alejandro.liebana.7e7@itb.cat",
    "didac.lloret.7e7@itb.cat",
    "yeray.lopez.7e7@itb.cat",
    "trishan.mizhquiri.7e6@itb.cat",
    "david.munoz.7e7@itb.cat",
    "andre.oyarzo.7e7@itb.cat",
    "saul.requena.7e7@itb.cat",
    "andrea.riba.7e7@itb.cat",
    "ruben.sanchez.7e7@itb.cat",
    "pol.sanchez.7e7@itb.cat",
    "taranpreet.singh.7e7@itb.cat",
    "rene.tubiera.7e7@itb.cat",
    "jordi.yu.7e7@itb.cat")
pick = random.randint(0, len(CORREO) - 1)
print(CORREO[pick])

"""
#RULE GRAFICA (no rula)
import turtle
import random

# Configuración inicial
turtle.speed(0)
turtle.bgcolor("white")
turtle.title("Ruleta")

# Colores
colores = ["red", "black", "green", "blue", "yellow", "orange", "purple", "pink"]

# Función para dibujar una caja de sección
def dibujar_seccion(color, tamaño):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(100, tamaño)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.end_fill()

# Dibujar las secciones de la ruleta
for _ in range(8):
    color = random.choice(colores)
    tamaño = random.randint(10, 60)
    dibujar_seccion(color, tamaño)

# Dibujar el indicador central
turtle.penup()
turtle.goto(0, -30)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# Mostrar la ventana de la ruleta
turtle.done()
"""