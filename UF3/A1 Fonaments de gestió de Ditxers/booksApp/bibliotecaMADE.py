"""
Description: Programa per guardar la informació dels diferents llibres que té una biblioteca

Usage:
Input --> Per teclat
3
Lorem
Ot Pi
56
Ipsum
Mar Om
77
Dolor
Lin Om
42
"""

import os

llibres = []

def get_input():
    global llibres
    num_llibres = int(input())
    for i in range(num_llibres):
        titol = input()
        autor = input()
        pagines = int(input())
        llibres.append((titol, autor, pagines))

def find_shortest_longest():
    shortest = llibres[0]
    longest = llibres[0]
    for llibre in llibres:
        if llibre[2] < shortest[2]:
            shortest = llibre
        elif llibre[2] > longest[2]:
            longest = llibre
    return shortest, longest

def add_to_library(file_path):
    global llibres
    with open(file_path, mode="w", encoding="utf-8") as file:
        file.write("Llibres\n--------\n\n")
        for llibre in llibres:
            file.write(f"{llibre[0]} - {llibre[1]} - {llibre[2]} pàgines\n")
        file.write("\n-----------\n")

def show_summary():
    global llibres
    total_llibres = len(llibres)
    shortest, longest = find_shortest_longest()

    print("Llibres\n--------")
    for llibre in llibres:
        print(f"{llibre[0]} - {llibre[1]} - {llibre[2]} pàgines")
    print("-----------\n")

    print(f"Total: {total_llibres} llibres")
    print(f"Llibre més curt: {shortest[0]} - {shortest[1]} - {shortest[2]} pàgines")
    print(f"Llibre més llarg: {longest[0]} - {longest[1]} - {longest[2]} pàgines")


get_input()
library = os.path.join('.', 'books.out')
add_to_library(library)
show_summary()
