"""
4/04/2024
Ayman Dghoughi Nouri
ASIXcB
M03 UF2 pp1
Descripció: programa principal, incloeix el menu i la funció principal.
"""
#region Imports -----------------------
import SignesPuntuacio
import Text
#endregion

#region Menu -----------------------
def menu():
    while True:
        result = ""
        options = ["1","2","3","4","5","6"]
        select = f"\n1 - Utilitat 1\n" \
                 f"2 - Utilitat 2\n" \
                 f"3 - Utilitat 3\n" \
                 f"4 - Utilitat 4\n" \
                 f"5 - Executar totes les utilitats\n" \
                 f"6 - Sortir de l'aplicació\n"
        print(select)
        choice = input("Selecciona una opción: ")
        match choice:
            case "1":
                lenght_clean, lenght = SignesPuntuacio.netejar_frase()
                result = SignesPuntuacio.quantitat(lenght_clean, lenght)
            case "2":
                text = SignesPuntuacio.netejar_frase()
                result = SignesPuntuacio.posició(text)
            case "3":
                text, shift = Text.cesar_input()
                result = Text.cesar_cipher(text, shift)
            case "4": result = Text.cesar_cipher()
            case "5":
                lenght_clean, lenght = SignesPuntuacio.netejar_frase()
                result = SignesPuntuacio.quantitat(lenght_clean, lenght)
                text = SignesPuntuacio.netejar_frase()
                result = SignesPuntuacio.posició(text)
                Text.cesar_cipher()
            case "6": exit(0)
            case _: menu()
        return print(result)
#enregion

#region main -----------------------
def main():
    menu()
if __name__ == '__main__':
    main()
#endregion