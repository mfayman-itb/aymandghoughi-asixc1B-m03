"""
   JAB Javier Amaya Boira
   ITB Institut Tecnològic de Barcelona
   04/05/2022
   10/04/2023
   ASIXc M03 UF3 Fitxers
   Tractament d'exceptions
"""

fitxer="noExixteis.cap"
try:
  f = open(fitxer, 'r')
# Fer moltes altres accions
# ...
except OSError as err:
  print('No es pot obrir   : ', fitxer)
  print('Missatge          : ', err)
  print('Missatge errno    : ', err.errno)
  print('Missatge strerror : ', err.strerror)
  print('Missatge filename : ', err.filename)
except ValueError:
   print("ERROR de tipos de dades")
except Exception as err:
   print(f"Unexpected {err=}, {type(err)=}")


print("\n\n\nPerò el programa continua igualment")



# EXCEPCIONS DE FITXERS

def main():
   try:
       f = open(FILE_NAME, "at", encoding="UTF-8")
       f.write(obtenirDataHora() + " " + "JAVI es genial" + "\n")
   except FileNotFoundError:
       print("Fitxer/Directory no trobat: " + FILE_NAME)
   except PermissionError:
       print("Error de permisos: " + FILE_NAME)
   except:
       print("Error inesperat")
   finally:
       f.close()
   print("Programa acabat")

main()