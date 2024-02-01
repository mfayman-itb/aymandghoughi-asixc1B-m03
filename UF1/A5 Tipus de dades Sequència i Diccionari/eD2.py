# Escriu un programa que llegeixi una cadena i mostri per pantalla el diccionari que conté com a entrada els caràcters de la cadena i com a valor de cada entrada, la quantitat d'aparicions del caràcter a la cadena.
string = input()
dicc = [character for character in string]
occ = {character:string.count(character) for character in dicc}
print(occ)
