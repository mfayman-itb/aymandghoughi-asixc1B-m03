"""
descripción: tiras un dado contra la maquina y tu numero sera el de la cara
opuesta a la que saques(tambiel la maquina). Luego dice quien gana.
"""
dado = int(input())
import random

if dado < 1 or dado > 6:
    print("ERROR")
else:
    dadoCOMPUTER = int(random.uniform(1, 7))

    if dado == 1:
        dado = 6
    elif dado == 6:
        dado = 1
    elif dado == 2:
        dado = 5
    elif dado == 5:
        dado = 2
    elif dado == 3:
        dado = 4
    elif dado == 4:
        dado = 3

    if dadoCOMPUTER == 1:
        dadoCOMPUTER = 6
    elif dadoCOMPUTER == 6:
        dadoCOMPUTER = 1
    elif dadoCOMPUTER == 2:
        dadoCOMPUTER = 5
    elif dadoCOMPUTER == 5:
        dadoCOMPUTER = 2
    elif dadoCOMPUTER == 3:
        dadoCOMPUTER = 4
    elif dado == 4:
        dadoCOMPUTER = 3

    print(f"número do jogador é {dado}.")
    print(f"o número do computador é {dadoCOMPUTER}.")

    if dado > dadoCOMPUTER:
        print("o jogador ganhou")
    elif dadoCOMPUTER < dado:
        print("o computador ganhou")
    else:
        print("gravata")
