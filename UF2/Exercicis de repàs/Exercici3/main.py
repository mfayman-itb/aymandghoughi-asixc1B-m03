import estadistiques
import cadenes
import utils

def estadistiques_menu():
    while True:
        utils.print_sub_menu(["Calcular mitjana", "Calcular mediana", "Calcular desviació estàndard", "Tornar al menú anterior"])
        option = utils.get_input("Selecciona una opció: ")
        if option == "1":
            print(estadistiques.calcular_mitjana())
        elif option == "2":
            print(estadistiques.calcular_mediana())
        elif option == "3":
            print(estadistiques.calcular_desviacio_estandard())
        elif option == "4":
            break
        else:
            print("Opció invàlida. Torna a intentar.")

def cadenes_menu():
    while True:
        utils.print_sub_menu(["Crazy Words", "És una frase palíndroma?", "Xifratge de Cèsar", "Tornar al menú anterior"])
        option = utils.get_input("Selecciona una opció: ")
        if option == "1":
            text = utils.get_input("Introduce un texto: ")
            words = cadenes.fix_punctuation(cadenes.check_input(text, option))
            result = cadenes.crazy_words(words)
            print("Texto resultante:", result)
        elif option == "2":
            # Lógica para la opción 2
            pass
        elif option == "3":
            # Lógica para la opción 3
            pass
        elif option == "4":
            break
        else:
            print("Opció invàlida. Torna a intentar.")

def main():
    while True:
        utils.print_menu(["Utilitats Estadístiques", "Utilitats de Cadenes", "Sortir de l’aplicació"])
        option = utils.get_input("Selecciona una opció: ")
        if option == "1":
            estadistiques_menu()
        elif option == "2":
            cadenes_menu()
        elif option == "3":
            print("Adéu!")
            break
        else:
            print("Opció invàlida. Torna a intentar.")

if __name__ == "__main__":
    main()
