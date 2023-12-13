num = int(input("Give me numbers: "))
suma = 0
count = 0
while num != 0:
    suma += num
    num = int(input("Give me numbers: "))
    count += 1
mitjana = suma / count
print(f"La suma dels nombres introduits es {suma}.")
print(f"La mitjana dels nombres introduits es {mitjana:.2f}.")

