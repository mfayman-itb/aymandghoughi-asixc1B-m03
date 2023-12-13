"""
descripción: Realitzar un programa que calculi quants diners estalviarà una persona en un any
"""
estalvi = int(input("Quant diner estalviaras aquest mes: "))
money = estalvi

for i in range(1, 13):
    print(f"Diners ahorrats fins ara: {money}\n")
    estalvi = int(input("Quant diner estalviaras aquest mes: "))
    money += estalvi
print(f"\nDiner estalviat aquest any: {money}, felicidades ya sabes ahorrar pou.")