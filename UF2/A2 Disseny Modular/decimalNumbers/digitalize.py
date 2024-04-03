def obtener_digito(num):
    if num == 0:
        return ["#####", "#   #", "#   #", "#   #", "#   #", "#   #", "#####"]
    elif num == 1:
        return ["  #  ", " ##  ", "# #  ", "  #  ", "  #  ", "  #  ", "#####"]
    elif num == 2:
        return ["#####", "    #", "    #", "#####", "#    ", "#    ", "#####"]
    elif num == 3:
        return ["#####", "    #", "    #", "#####", "    #", "    #", "#####"]
    elif num == 4:
        return ["#   #", "#   #", "#   #", "#####", "    #", "    #", "    #"]
    elif num == 5:
        return ["#####", "#    ", "#    ", "#####", "    #", "    #", "#####"]
    elif num == 6:
        return ["#####", "#    ", "#    ", "#####", "#   #", "#   #", "#####"]
    elif num == 7:
        return ["#####", "    #", "    #", "    #", "    #", "    #", "    #"]
    elif num == 8:
        return ["#####", "#   #", "#   #", "#####", "#   #", "#   #", "#####"]
    elif num == 9:
        return ["#####", "#   #", "#   #", "#####", "    #", "    #", "#####"]
    else:
        return ["     ", "     ", "     ", "     ", "     ", "     ", "     "]

def obtener_formato_numerico(num):
    num_str = str(abs(num))
    digitos = [obtener_digito(int(d)) for d in num_str]
    formato_numerico = [" ".join(row) for row in zip(*digitos)]
    return "\n".join(formato_numerico)

def imprimir_numero(num):
    formato_numerico = obtener_formato_numerico(num)
    if num < 0:
        formato_numerico = "\n".join([fila[::-1] for fila in formato_numerico.split("\n")])
    print(formato_numerico)

def main():
    numero = int(input("Introduce un número: "))
    imprimir_numero(numero)

if __name__ == "__main__":
    main()

