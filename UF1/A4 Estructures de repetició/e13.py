"""
descripción: programa que mostrarà el total d’hores treballades i el sou total.
"""
souH = int(input("Introduce el sueldo por hora: "))
hora = 0
horaT = 0

for i in range(1, 7):
    hora = int(input("Cuantas horas has trabajado hoy? "))
    horaT += hora
    sueldoT = horaT * souH
print(f"Has treballat {horaT} horas y tu sueldo total es de {sueldoT}€.")