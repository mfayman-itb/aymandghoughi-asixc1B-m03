"""
descripción: calcular el importe dependiendo el sitio
"""
place = input("A quina zona ho enviem: ").lower()
weight = int(input("Quin es el seu pes: "))

if weight > 5:
    print("Error, el pes supera els 5 kg.")
if place == "america del nord":
    importe = 24 * weight
elif place == "america central":
    importe = 20 * weight
elif place == "america del sud":
    importe = 21 * weight
elif place == "europa":
    importe = 10 * weight
elif place == "asia":
    importe = 18 * weight
else:
    print("Eres bobi o que pon una zona correcta.")
print(f"El importe final es de {importe}€.")