filename = "prices"

def see_the_cheapest():
    preus = []
    with open(filename, 'r') as file:
        for line in file:
            for price in line.split():
                preus.append(int(price))
    return preus


def trobar_preu_mes_baix(preus):
    preu_mes_baix = preus[0]
    for preu in preus:
        if preu < preu_mes_baix:
            preu_mes_baix = preu
    return preu_mes_baix

def mostrar_preu_mes_baix(preu):
    print("El producto más económico vale:", preu, "€")

