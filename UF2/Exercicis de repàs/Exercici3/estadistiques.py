import math

def calcular_mitjana():
    mitj = input("Introdueix una llista de números: ").split()
    mitj = [float(num) for num in mitj]  # Convertir los elementos de la lista a números flotantes
    longitud = len(mitj)
    suma = sum(mitj)
    mitj = suma / longitud
    return mitj

def calcular_mediana():
    med = input("Introduce una lista de números: ").split()
    med = [float(num) for num in med]  # Convertir los elementos de la lista a números flotantes
    longitud = len(med)
    med.sort()
    if longitud % 2 == 0:
        mediana = (med[longitud // 2 - 1] + med[longitud // 2]) / 2
    else:
        mediana = med[longitud // 2]
    return mediana

def calcular_desviacio_estandard(nums):
    mitjana = calcular_mitjana()
    suma_cuadrados_diff = sum((x - mitjana) ** 2 for x in nums)  # Calcular la suma de los cuadrados de las diferencias
    desviacio_estandard = math.sqrt(suma_cuadrados_diff / (len(nums) - 1))  # Calcular la desviación estándar
    return desviacio_estandard
