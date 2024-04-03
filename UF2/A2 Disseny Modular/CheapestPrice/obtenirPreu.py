def obtenir_preus():
    try:
        preus = input().split()
        preus = [int(preu) for preu in preus if preu != '-1'] #recorre todos los elementos en la lista preus, los convierte en enteros y los agrega a una nueva lista, excluyendo -1
        return preus
    except Exception as e:
        print(e)
        print("Introdueix només números!")

def trobar_preu_mes_baix(preus):
    preu_mes_baix = preus[0]
    for preu in preus:
        if preu < preu_mes_baix:
            preu_mes_baix = preu
    return preu_mes_baix

def mostrar_preu_mes_baix(preu):
    print("El producte més económic val:", preu, "€")