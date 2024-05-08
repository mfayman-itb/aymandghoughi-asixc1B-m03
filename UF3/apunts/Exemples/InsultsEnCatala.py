"""
   Autor:      Javier Amaya Boira
               José Luis Álvarez Casas

   Data:       12/01/2022
               28/04/2022
               29/03/2023
               07/04/2024
               22/04/2024

   ASIXc M03   UF1 Fonaments de programació
               UF2 Disseny Descendent i Modular
               UF3 Arxius

   Exercici:   Insults en català
               Pr5 - Tipus de dades Seqüència i Diccionari

   Programa de traducció d’insults. Crear un array de dues dimensions amb els insults en català
   i afegir la traducció en castellà, anglès i kli.dic
   El programa, demanarà a l’usuari que escrigui per teclat un insult, en català, i el mostrarà traduït a castellà,
   anglès  i kli.dic.
"""
import systemColors

CAT=0; ESP=1; ANG=2; KLI=3
INSULTS = [[], [], [], []]

def carregarDiccionari():
   fCat = open("Cat.dic", "rt", encoding="UTF-8")
   fEsp = open("Esp.dic", "rt", encoding="UTF-8")
   fAng = open("Ang.dic", "rt", encoding="UTF-8")
   fKli = open("kli.dic", "rt", encoding="UTF-8")

   #TODO Convertir en una nova fucnció: recorregut indexat per a tots els idiomes possibles
   #     Obtenir llistat de tots els fitxer d'idioma *.dic
   #     Crear estructura "matriu" per emmagatzemar tots els idiomes
   #     Carregar idiomes  a la matriu

   for linea in fCat:
       linea = linea.strip() #The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
       INSULTS[CAT].append(linea)
   fCat.close()


   for linea in fEsp:
       linea = linea.strip()
       INSULTS[ESP].append(linea)
   fEsp.close()


   for linea in fAng:
       linea = linea.strip()
       INSULTS[ANG].append(linea)
   fAng.close()


   for linea in fKli:
       linea = linea.strip()
       INSULTS[KLI].append(linea)
   fKli.close()



def llegirInsult():
   return input("insult ? ")
def traduirInsult(parametreInsult):
   traduccio=""
   for i in range(len(INSULTS[0])):
       if parametreInsult.upper() == INSULTS[0][i]:
           traduccio= INSULTS[1][i], INSULTS[2][i], INSULTS[3][i]
    #TODO: Tractar el cas quan NO es troba l'insult

   return traduccio
def mostrarTraduccio(traduccio):
   print(systemColors.CBLUE,end="")
   print(f"{traduccio[0]}\t{traduccio[1]}\t{traduccio[2]}")
   print(systemColors.CBLACK,end="")
def tractarExcepcio(e):
   print(systemColors.CITALIC+ systemColors.CBLACK+systemColors.CREDBG2,end="")
   print(f"EXCEPCIÓ: {e=}, {type(e)=}")
   print(f"EXCEPCIÓ:\n Missatge: {e} \nTipus {type(e)=}")
   print(systemColors.CBLACK,end="")

# Main ------------- només 4 passos -------------------------------------
    #TODO: convertir a una funció main()
try:
   carregarDiccionari()
   insult=llegirInsult()
   traduccio=traduirInsult(insult)
   mostrarTraduccio(traduccio)
except Exception as e:
   tractarExcepcio(e)