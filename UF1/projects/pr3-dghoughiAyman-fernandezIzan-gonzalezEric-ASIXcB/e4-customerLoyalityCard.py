"""
Eric González, Izan Fernandez , Ayman Dghoughi
08/11/2023
M03 UF1 A3
Descripció: Programa que demana l'import d'una factura, amb iva inclòs i
calcula l'import amb descompte tenint en compte algunes condicions.
"""

imp = float(input("Quin es l'import de la teva factura amb IVA inclòs? "))
targ_cli = str(input("Tens targeta client si/no? ")).lower()

if targ_cli == "si" and imp >= 100:
    descompte = 21 % imp
    preu = imp - descompte
    print("El preu final amb descompte es:", preu)
else:
    print("No tens descompte, i per tant el preu final és:", imp)