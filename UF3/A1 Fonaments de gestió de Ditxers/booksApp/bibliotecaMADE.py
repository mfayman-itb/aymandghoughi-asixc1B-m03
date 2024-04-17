import os

llibres =[]
library = os.path.join('.','books.out')

def get_input():
    global llibres
    num_llibres = int(input())
    for i in range(num_llibres):
        titol = input()
        autor = input()
        pagines = int(input())
        llibres.append((titol, autor, pagines))

def addLECTO():
    global llibres
    with open(library, mode="w",encoding="utf-8") as file:
        file.write("Llibres\n--------\n\n")
        for llibre in llibres:
            file.write(f"{llibre[0]} - {llibre[1]} - {llibre[2]} pàgines\n")
        file.write("\n-----------\n")

get_input()