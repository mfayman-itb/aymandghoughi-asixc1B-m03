def obtenir_preus():
    preus = []
    while True:
        preu = input()
        if preu == '-1':
            break
        preus.append(int(preu))
    return preus

def trobar_preu_mes_baix(preus):
    preu_mes_baix = preus[0]
    for preu in preus:
        if preu < preu_mes_baix:
            preu_mes_baix = preu
    return preu_mes_baix

def mostrar_preu_mes_baix(preu):
    print("El producto más económico vale:", preu, "€")

def main():
    preus = obtenir_preus()
    preu_mes_baix = trobar_preu_mes_baix(preus)
    mostrar_preu_mes_baix(preu_mes_baix)

if __name__ == "__main__":
    main()
