"""
En aquest exemple, primer definim el contingut JSON que volem escriure en un fitxer. Després, utilitzem la funció json.dump() per escriure el contingut en un fitxer anomenat exemple.json.

A continuació, utilitzem la funció json.load() per llegir el contingut JSON del fitxer exemple.json i assignar-lo a la variable x.

Finalment, imprimim el contingut JSON amb la funció json.dumps() i utilitzem l'argument indent per especificar la quantitat d'espais que volem utilitzar per a l'indentació del contingut.
"""
import json
# definim el contingut JSON
x = {
   "name": "John",
   "age": 30,
   "married": True,
   "divorced": False,
   "children": ("Ann", "Billy"),
   "pets": None,
   "cars": [
       {"model": "BMW 230", "mpg": 27.5},
       {"model": "Ford Edge", "mpg": 24.1}
   ]
}
# escriure el contingut JSON en un fitxer
with open('exemple.json', 'w') as f:
   json.dump(x, f)

# llegir el contingut JSON d'un fitxer
with open('exemple.json', 'r') as f:
   x = json.load(f)

# imprimir el contingut JSON

print(json.dumps(x, indent=4))

# TIP Ctrl + Alt + L formatear archivo json

# Convertir JSON a Python
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])


# Convertir Python a JSON
import json
# a Python object (dict):
x = {
 "name": "John",
 "age": 30,
 "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)


#Convert Python objects into JSON strings, and print the values:
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


#Convert a Python object containing all the legal data types:
import json
x = {
 "name": "John",
 "age": 30,
 "married": True,
 "divorced": False,
 "children": ("Ann","Billy"),
 "pets": None,
 "cars": [
   {"model": "BMW 230", "mpg": 27.5},
   {"model": "Ford Edge", "mpg": 24.1}
 ]
}
print(json.dumps(x))


#Use the indent parameter to define the numbers of indents: (facilitar lectura)
json.dumps(x, indent=2)

#Use the separators parameter to change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))

#Use the sort_keys parameter to specify if the result should be sorted or not: (ordenar)
json.dumps(x, indent=4, sort_keys=True)

