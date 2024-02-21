try:
    preus = input().split()
    preus = [float(i) for i in preus]
    total = 0
    while len(preus) != 10:
        preus = input().split()
        preus = [float(i) for i in preus]

    for preu in preus:
        total += preu
    maximo = print(f'Maxim: {max(preus):.2f}')
    mitjana = print(f'Mitjana: {total / (len(preus)):.2f}')
except (TypeError, ValueError) as e:
    print("Introduce precios en numeros reales.")
    print(e)