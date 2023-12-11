'''
Ayman Dghoughi, Nizar El Khoulfi, Ian Diaz
11/10/23
ASIXc M03 UF1 A2
Descripció: Programa per calcular la superfície d'una pizza a partir del diàmetre
'''

try:
    print("Amplada de l'habitació?")
    amplada = float(input())

    print("Llargada de l'habitació?")
    llargada = float(input())

    print("Alçada de l'habitació?")
    alçada = float(input())

    volum = float(amplada * llargada * alçada)

    print(f"El volum de l'aula és {volum:.2f} m³")

except Exception as e:
    print(e)
    exit(1)