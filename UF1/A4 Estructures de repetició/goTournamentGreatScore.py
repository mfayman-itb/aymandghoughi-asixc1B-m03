punts = 0
nomAux = input("Escriu el nom del participant: ")

while(nomAux.upper() != "END"):
   puntsAux = int(input("Escriu la seva puntuació: "))
   if puntsAux >= punts:
       nom = nomAux
       punts = puntsAux
   nomAux = input("Escriu el nom del participant: ")
print(nom + ":" + " " + str(punts))
