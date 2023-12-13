"""
descripción: Imprimeix "Excel·lent", "Notable", "Bé", "Suficient", "Suspès", "Nota invàlida" segons  la nota
numèrica introduïda.
"""
nota = float(input("Introduce tu nota: "))

if nota >=1 and nota <= 4:
    print("Suspenso")
elif nota == 5:
    print("Suficiente")
elif nota == 6:
    print("Bien")
elif  nota == 7 or nota == 8:
    print("Notable")
elif nota == 9 or nota == 10:
    print("Sobresaliente")
else:
    print("Nota incorrecta")
