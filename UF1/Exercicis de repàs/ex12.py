# Métodos de cadenas de caracteres

cad = "Hola Mundo :-)"

print(cad.upper())
print(cad.lower())



# busqueda en la cadena

cad = "     bienvenido a mi aplicación          "

print(cad.count("a"))
print(cad.count("a", 16))
print(cad.count("a", 10, 16))
print(cad.find("mi"))
print(cad.find("xx"))

# métodos de validación

print(cad.startswith("b"))
print(cad.endswith("ción"))

# otros

print(cad.replace("a", "U"))

# quita los espacios del inicio y fin

cadenaSinEspacios = cad.strip()

print(cadenaSinEspacios)

cadenaConCeros = "000012345678900000"

print(cadenaConCeros.strip("0"))

# Separar por el separardor :
hora = "12:23:12"

print(hora.split(":"))  # ['12', '23', '12']

minuto = hora.split(":")[1]

print(minuto)

texto = "Linea 1\nLinea 2\nLinea 3\n"

print(texto.splitlines())