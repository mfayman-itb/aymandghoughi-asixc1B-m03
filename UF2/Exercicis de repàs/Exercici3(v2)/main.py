import estadistica
import cadenas
result = ""
def menu():
    result = ""
    options = ["1","2","3"]
    select = f"\n1 - Utilidades Estadísticas\n" \
             f"2 - Utilidades de Cadenas\n" \
             f"3 - Salir de la aplicación\n"
    print(select)
    choice = input("Selecciona una opción: ")
    match choice:
        case "1": result = menuStad()
        case "2": result = menuStrings()
        case "3": exit(0)
        case _: menu()
    return print(result)

def menuStad():
    options = ["1.1","1.2","1.3","1.4"]
    select = f"\n1.1 - Calcular media\n" \
             f"1.2 - Calcular mediana\n" \
             f"1.3 - Calcular desviación estándar\n" \
             f"1.4 - Volver al menú anterior\n"
    print(select)
    choice = input("Selecciona una opción: ")
    match choice:
        case "1.1": result = estadistica.calcMitjana()
        case "1.2": result = estadistica.calcMediana()
        case "1.3": result = estadistica.calcDesv()
        case "1.4": menu()
        case _: menuStad()
    return result

def menuStrings():
    options = ["2.1","2.2","2.3","2.4"]
    select = f"\n2.1 - Crazy Words\n" \
             f"2.2 - Es palindromo?\n" \
             f"2.3 - Cifrado de Cesar\n" \
             f"2.4 - Volver al menú anterior\n"
    print(select)
    choice = input("Selecciona una opción: ")
    match choice:
        case "2.1":
            text = cadenas.get_input()
            cadenas.check_input(text, "crazywords")
            clean = cadenas.fix_punctuation(text)
            result = cadenas.disorder_words(clean)
        case "2.2":
            text = cadenas.get_input()
            cadenas.check_input(text, "palindromo")
            result = cadenas.palindrom(text)
        case "2.3": result = cadenas.caesarCipher()
        case "2.4": menu()
        case _: menuStrings()
    return result
def main():
    menu()
if __name__ == '__main__':
    main()