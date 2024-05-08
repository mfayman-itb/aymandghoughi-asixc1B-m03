"""
    JAB Javier Amaya Boira
  ITB Institut Tecnològic de Barcelona
  14/03/2023
  29/03/2023
  15/04/2024
  ASIXc M03 UF3 Fitxers
  Exemple: Ruta a un diretori

EXECUTAR:
   Des del TERMINAL:
   /workspace/javieramaya-asix-m03/UF3/Exemples/25RutaRelativa/python3  rutaADirectory.py
"""

import os

#Linux "./Dades/prova.out"
# Windows ".\Dades\prova.out"
PATH_NAME = os.path.join(".","Dades")
FILE_NAME = os.path.join(PATH_NAME,"prova.out")

def obtenirDataHora():
   from datetime import datetime
   # datetime object containing current date and time
   now = datetime.now()
   # dd/mm/YY H:M:S
   dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
   return dt_string


# --- Main --------------------------------------------------------------------

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

# --- End ---------------------------------------------------------------------

# Fem-la servir per preguntar quin és el directori actual de treball:
#Directori actual de treball: /home/sjo
print("Directori actual de treball:", os.getcwd())

# Per a saber si una ruta absoluta indica un directori fem (aquest exemple és per a Windows, noteu les dobles barres):
#'c:\Windows' és un directori?  True
print("'c:\\Windows' és un directori? ", os.path.isdir("c:\\Windows"))

# El mateix per a una ruta relativa:
#'../' és un directori?  True
print("'../' és un directori? ", os.path.isdir("../"))

# Notar que aquest exemple funciona tant en Linux com a Windows: la llibreria Python fa la traducció de "../" a "..\" de manera transparent.
# Per saber si una ruta absoluta indica un fitxer.
#'/etc/profile' és un fitxer?  True
print("'/etc/profile' és un fitxer? ", os.path.isfile("/etc/profile"))

# El mateix amb una ruta relativa:
#'./README.md' és un fitxer?  True
print("'./README.md' és un fitxer? ", os.path.isfile("./README.md"))


# PERMISOS

# Un altre tipus d'operació típica que podem fer és preguntar pels permisos d'un fitxer o directori:
# Comprovar els permisos del fitxer, per exemple, de lectura ...
#Tinc permisos de lectura a './README.md'?  True
print("Tinc permisos de lectura a './README.md'? ", os.access("./README.md", os.R_OK))


# ... d'escriptura ...
#Tinc permisos d'escriptura a './README.md'?  True
print("Tinc permisos d'escriptura a './README.md'? ", os.access("./README.md", os.W_OK))


# ... o d'execució
# Tinc permisos d'execució a '../fitxers/script1.sh'?  True
print("Tinc permisos d'execució a '../fitxers/script1.sh'? ", os.access("../fitxers/script1.sh", os.X_OK))


# Òbviament, podem fer les mateixes preguntes sobre un directori. Per ser breus, només
# posarem l'exemple per als permisos de lectura
#Tinc permisos de lectura a '/home/sjo'?  True
print("Tinc permisos de lectura a '%s'? " % (os.getcwd()), os.access(os.getcwd(), os.R_OK))


# LLISTAR FITXERS

import os

# Llistem els fitxers i directoris d'un directori donat.
directori = input("Entra una ruta absoluta o relativa a un directori: ")
llistaItems = os.listdir(directori)
print("Fitxers i directoris trobats a '%s': " % directori)

for item in llistaItems:
   rutaFitxer= os.path.join(directori, item)
   if os.path.isfile(directori + "/" + item):              # Windows o Linux?
       print(f"FITXER\t\t {rutaFitxer}")
   else:
       print(f"DIRECTORI\t {rutaFitxer}")


# ESBORRAR

#Esborrar un fitxer

import os
f = open("ArxiuPerEsborrar.txt", "w") # Per crear el fitxer, abans d'eborrar-lo
f.close()

os.remove("ArxiuPerEsborrar.txt")


#Esborrar un fitxer de forma segura
import os
nomArxiu="ArxiuPerEsborrar.txt"
f = open(nomArxiu, "w")  # Per crear el fitxer, abans d'esborrar-lo
f.close()

if os.path.exists(nomArxiu):
   os.remove(nomArxiu)
else:
 print(f"No existeix el FITXER: {nomArxiu}")


#Esborrar un directori de forma segura
nomDirectori ="D1"
if os.path.exists(nomDirectori):
   os.rmdir(nomDirectori)
else:
   print(f"No existeix el DIRECTORI: {nomDirectori}")


# OBTENIR INFO DEL FITXER STAT

#obtenir mida
import os, stat
statinfo = os.stat('somefile.txt')
print(statinfo.st_size)
print(statinfo.st_mtime)


# CHMOD

#Modificar atributs d'un fitxer
# Set to user rw, else r
testFile = "TestAtributes.txt"
os.chmod(testFile, 0o644)
# No-one can write
os.chmod(testFile, 0o444)


#Establir diferents permisos, fent servir l'operador OR | para combinar els "flags" dels permisos
os.chmod(testFile, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR) #-rwx------ TestAtributes.txt


#On Windows, the following file attribute constants are available for use when testing bits in the st_file_attributes member returned by os.stat().
os.chmod(testFile,stat.FILE_ATTRIBUTE_READONLY)


# MKDIR
import os
path = 'tempDir'
os.mkdir(path)


# Create target Directory if don't exist
dirName="DD"
if not os.path.exists(dirName):
   os.mkdir(dirName)
   print("Directory " , dirName ,  " Created ")
else:
   print("Directory " , dirName ,  " already exists")


# IF DIRECTORY EXISTS

# Create directory
dirName = 'tempDir'
try:
  # Create target Directory
   os.mkdir(dirName)
   print("Directory " , dirName ,  " Created ")
except FileExistsError:
   print("Directory " , dirName ,  " already exists")