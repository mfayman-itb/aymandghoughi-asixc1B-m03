"""
Description: programa que simula un llum, amb les accions:
--> TURN ON: Encén el llum
--> TURN OFF: Apaga el llum
--> TOGGLE: Canvia l'estat del llum
--> END: Finalitza la seqüència d'accions. Warning si el fitxer no acaba amb END

Usage:
Input --> File
Output --> Terminal
"""

import os
from lamp_actions import *

def main():
    light = False
    filename = os.path.join('.', 'lampinput')
    try:
        with open(filename, 'r') as file:
            for line in file:
                action = line.strip().upper()
                print("> " + action)
                if action == "TURN ON":
                    light = turn_on(light)
                elif action == "TURN OFF":
                    light = turn_off(light)
                elif action == "TOGGLE":
                    light = toggle(light)
                elif action == "END":
                    break
                else:
                    print("Acción no válida:", action)
    except FileNotFoundError:
        print("The file", filename, "not exist.")
    else:
        if action != "END":
            print("\nWARNING - The file doesn't ended with the action 'END'.")

if __name__ == "__main__":
    main()
