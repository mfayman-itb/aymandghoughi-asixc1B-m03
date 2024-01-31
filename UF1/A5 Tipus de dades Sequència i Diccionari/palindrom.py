# re.sub(patron, reemplazo, cadena)
import re
from unidecode import unidecode

palindrom = input().lower()
pal = re.sub(r'[^a-z0-9]', '', unidecode(palindrom))
revrs = pal[::-1]

if revrs == pal:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
