"""
Exemple: ordenarNumeros.py
        Ordenació de nombres enters a una llista
"""
#region Definició de constants i variables
MAX_NOMBRES = 10 # Constant amb la quantitat de nombres enters a demanar a l'usuari
llistaNombres = [] # Llista que contindrà els nombres a llegir del teclat
#endregion

# region Definició de funcions
def llegirLlista():
   """
   Funció que demana a l'usuari que entri els numeros,
   i els afegeix a la llista "llistaNombres"
   """
   print("Escriu 10 valors enters i prem retorn.")
   try:
       for i in range(MAX_NOMBRES):
           nombre = int(input("Nombre [%d]: " % (i + 1)))
           llistaNombres.append(nombre)
   except ValueError:
       print("ERROR. Has d'introduir un nombre enter.")

def ordenarLlista():
   # Ordena els nombres presents a la llista "llistaNombres"
   temporal = 0
   for i in range(len(llistaNombres)):
       for j in range(i + 1, len(llistaNombres)):
           if llistaNombres[i] > llistaNombres[j]:
               temporal = llistaNombres[i]
               llistaNombres[i] = llistaNombres[j]
               llistaNombres[j] = temporal

def mostrarLlista():
   # Funció per mostrar la llista "llistaNombres" per pantalla.
   if len(llistaNombres)>0:
       print("La llista ordenada és: ", end="")
       for i in range(len(llistaNombres)):
           if i == len(llistaNombres) - 1:
               print(llistaNombres[i], end="]")
           else:
               print(llistaNombres[i], end=",")
   else:
       print("La llista està buida.")
# endregion

# region Codi principal del programa
llegirLlista()
ordenarLlista()
mostrarLlista()
# endregion