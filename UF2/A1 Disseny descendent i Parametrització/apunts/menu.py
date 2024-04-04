# region Importar Biblioteques ------------------------------------------------
from datetime import date
from datetime import datetime
from time import sleep
# endregion

# region Definició de funcions ------------------------------------------------
def obteOpcio():
   BLAU= "\033[34m"
   NEGRE="\33[30m"
   print(BLAU+"1.- Primera opció" )
   print("2.- Millor opció")
   print("3.- Jo triaria aquesta")
   print("4.- La millor opció")
   print("5.- Sortir"+NEGRE)
   return int(input("Opció:? "))

def opcioPrimera():
   print("Primera opció\n")
   sleep(2)

def opcioMillor():
   print("Millor opció\n")
   sleep(2)

def opcioJoTriariaAquesta():
   print("Jo triaria aquesta\n")
   sleep(2)

def opcioLaMillor():
   print("La millor opció\n")
   sleep(2)

def tractarError(missatge):
   # Obtenir la data del sistema i l'hora
   avui = date.today()
   ara = datetime.now()
   # Formatar la data i l'hora: month, day and year
   avui = avui.strftime("%B %d, %Y")
   # dd/mm/YY H:M:S
   ara = ara.strftime("%d/%m/%Y %H:%M:%S")
   """
   # dd/mm/YY
   avui = avui.strftime("%d/%m/%Y")
   # mm/dd/y
   avui = avui.strftime("%m/%d/%y")
   # Month abbreviation, day and year
   avui = avui.strftime("%b-%d-%Y")
   """
   # Mostrar missatge
   print("========================")
   print(f"{avui}\n{ara}\nERROR: {missatge}")
   print("========================\n")

def tractamentFinal():
   CYAN= "\033[35m"
   for i in range(5):
       print(".", end="")
       sleep(1)
   print(CYAN+ "\tSee you")
# endregion

# region Programa principal ---------------------------------------------------

# Mostrem el menú i demanem quina opció es vol executar
opcio = obteOpcio()

# Mentre no ens demanin sortir, atenem a l'opció triada
while opcio != 5:
   if opcio < 1 or opcio > 4:
       tractarError("opció no valida\n")
   else:
       if opcio == 1:
           opcioPrimera()
       elif opcio == 2:
           opcioMillor()
       elif opcio == 3:
           opcioJoTriariaAquesta()
       else: #opcio == 4:
           opcioLaMillor()
   # tornem a presentar el menú i a llegir l'opció triada
   opcio = obteOpcio()

# Tractament final
tractamentFinal() #Crtl+B --> Go To Definition
# endregion