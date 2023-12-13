"""
descripción: comprueba si esta en mayusculas o minusculas
"""
cadena = input("Escribe lo que quieras en minusculas o en mayusculas: ")

if cadena == cadena.upper():
    print("El mensaje estaba en mayusculas a que si")
elif cadena == cadena.lower():
    print("El mensaje estaba en minusculas a que si")
else:
    print("No vale unas en mayuscula y otras en minuscula pou")
