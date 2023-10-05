"""
Ayman Dghoughi Nouri
M03 UF1
04/10/2023
Descripció: L'usuari escriu un número enter. "Printa" per pantalla el número següent.
Per exemple, si entra el 4. El programa ha de mostrar la frase "Després ve el 5".
"""
try:
    nbr = int(input("Introdueix un valor: "))
    nxt_nbr = nbr + 1
    print("Després ve el ", str(nxt_nbr))
    print("Program completed")
except Exception as e:
    print(e)
    exit(1)