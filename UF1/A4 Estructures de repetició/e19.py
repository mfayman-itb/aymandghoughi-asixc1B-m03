"""
descripción: menu de opciones con sugerencias
"""
try:
    num = 0
    while num != 5:
        print("1. Liteartura\n2. Cinema\n3. Música\n4. Videojocs\n5. Sortir\n")
        num = int(input("Selecciona una opcio: "))

        if num == 1:
            print("- Don Quijote\n- Harry Potter\n- El Extrangero\n")
        elif num == 2:
            print("- Jarhead\n- Requiem for a Dream\n- (500)Days of Summer\n- Donnie Darko\n")
        elif num == 3:
            print("- Kanye West\n- Travis Scott\n- The Smiths\n- Kendrick Lamar\n")
        elif num == 4:
            print("- Dark Souls\n- Bloodborne\n- Elden Ring\n- Sekiro\n")
        elif num == 5:
            print("Adeu fins a la proxima.")
        else:
            print("Eres bobo o que pon un numero de las opciones.\n")
except Exception as e:
    if ValueError:
        print("Si us plau, introdueix només nombres enters.")
    else:
        print(e)
