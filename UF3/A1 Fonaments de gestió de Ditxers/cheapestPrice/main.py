"""
Description: programa que donada la llista de preus (sense decimals) de tot de productes, retorni el preu del producte més baix. La ruta al fitxer serà introduïda per teclat.

Usage:
Input --> File
Output --> Terminal
"""

from cheap import *

def main():
    preus = see_the_cheapest()
    preu_mes_baix = trobar_preu_mes_baix(preus)
    mostrar_preu_mes_baix(preu_mes_baix)

if __name__ == "__main__":
    main()