"""
descripción: te dice el dia de la semana en 3 idiomas
"""
dia = int(input("Que dia bobo? "))
idioma = input("Dime en que idioma lo quieres pou, ingles, catalan o castellano? ").lower()

if idioma == "catalan":
    if dia == 1:
        print("dilluns")
    elif dia == 2:
        print("dimarts")
    elif dia == 3:
        print("dimecres")
    elif dia == 3:
        print("dijous")
    elif dia == 5:
        print("VIERNEEEEEEEES")
    elif dia == 6:
        print("disabte")
    elif dia == 7:
        print("its sunday...")
    else:
        print("ese dia de la semana te lo has inventado bobi.")

if idioma == "angles" or "english" or "ingles":
    if dia == 1:
        print("monday")
    elif dia == 2:
        print("tuesday")
    elif dia == 3:
        print("wenesday")
    elif dia == 3:
        print("thursdat")
    elif dia == 5:
        print("friday")
    elif dia == 6:
        print("saturday")
    elif dia == 7:
        print("its sunday...")
    else:
        print("ese dia de la semana te lo has inventado bobi.")

if idioma == "castellano" or "castella" or "spanish":
    if dia == 1:
        print("lunes")
    elif dia == 2:
        print("martes")
    elif dia == 3:
        print("miercoles")
    elif dia == 3:
        print("jueves")
    elif dia == 5:
        print("viernes")
    elif dia == 6:
        print("sabado")
    elif dia == 7:
        print("its domingo...")
    else:
        print("ese dia de la semana te lo has inventado bobi.")
