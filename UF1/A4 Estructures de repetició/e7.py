"""
descripción: programa que mostri la taula de multiplicar d'un número introduït per teclat.
"""
num = int(input("Hasta que tabla quieres ver: "))

for i in range(num + 1):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print()
