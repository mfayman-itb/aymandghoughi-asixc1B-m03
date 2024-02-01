# Crearem un programa on es declararà una variable de tipus diccionari on es guardarà els preus per quilo de diferents fruites.
try:
    frutas = {
        'Manzanas': 5.2,
        'Peras': 5,
        'Poya': 89.9,
        'Guebos': 70.4,
        'Poyaiguebos': 150.2
    }
    choice = 1
    while choice != 2:
        try:
            cons = input("Introduce <fruta> <kilos>: ").split()
            fruta, kilos = cons[0].capitalize(), int(cons[1])
            print(f'Precio de {kilos}Kg de {fruta} = {kilos * frutas[fruta]:.2f}')
            choice = int(input("\n1.\tContinuar\n2.\tSalir."))
        except IndexError:
            print("Introduce una fruta y los kilos vendidos.")
except Exception as e:
    if TypeError:
        print("Introduce valores de tipo correcto.")
    print(e)