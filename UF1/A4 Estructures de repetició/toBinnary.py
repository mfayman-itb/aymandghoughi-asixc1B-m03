"""
descripción: Escriu un programa que llegeixi un nombre natural més petit que 256 i escrigui la seva representació en binari.
"""
num = int(input())
ye = ""

while(num > 0 and num <= 256):
    damn = num % 2
    ye = str(damn) + ye
    num = num // 2
print(ye)
