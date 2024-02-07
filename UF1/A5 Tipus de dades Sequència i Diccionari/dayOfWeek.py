"""
try:
    weekCA = ["dilluns", "dimarts", "dimecres", "dijous", "divendres", "disabte", "diumenge"]
    weekEN = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    weekSP = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    dia = int(input("Introdueix un num de la setmana: ")) -1
    lan = input("Idioma en/ca/sp? ").lower()
    if dia >= 1 and dia <= 7:
        if lan == "en":
            print(weekEN[dia])
        elif lan == "sp":
            print(weekSP[dia])
        elif lan == "ca":
            print(weekCA[dia])
except Exception as e:
    print(e)
"""


try:
    weekCA = ["dilluns", "dimarts", "dimecres", "dijous", "divendres", "disabte", "diumenge"]
    weekEN = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    weekSP = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    dia = int(input("Introdueix un num de la setmana: ")) - 1
    while dia < 0 or dia >= 7:
        dia = int(input("Introdueix un num valid: ")) - 1
    print(weekEN[dia], weekCA[dia], weekSP[dia])
except Exception as e:
    print(e)



"""
try:
week = [["lunes", "dilluns", "monday"], ["martes", "dimarts", "tuesday"], ["miercoles", "dimecres", "wednesday"]]
dia = int(input())
if dia >= 1 and dia <= 7:
    print(week[dia])
"""