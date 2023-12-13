"""
descripción: que tipo de triangulo es
"""
seg1 = int(input("Introduce el valor del primer segmento: "))
seg2 = int(input("Introduce el valor del primer segmento: "))
seg3 = int(input("Introduce el valor del primer segmento: "))

if seg1 == seg2 and seg2 == seg3:
    print("Triangulo equilatero")
elif seg1 != seg2 and seg2 != seg3 and seg3 != seg1:
    print("Triangulo escaleno")
elif seg1 != seg2 and seg2 == seg3:
    print("Triangulo isoceles")
else:
    print("Triangulo isoceles")