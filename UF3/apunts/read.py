# obrim el fitxer amb la funció "open"
>>> f = open('un_poble.txt', mode='rt', encoding='utf-8')

# llegir els 20 primers caràcters del fitxer
>>> f.read(20)
'La mare era mestra.\n'

# llegir la resta del fitxer
>>> f.read()
'Vivíem tots dos sols. No teníem ni vàter.\nDamunt de la casa, les estrelles'

# Finalment, tanquem el fitxer
>>> f.close()

# modes d'obertura

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exist

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

"""
  JAB Javier Amaya Boir
  ITB Institut Tecnològic de Barcelona
  14/03/2023
  29/03/2023
  ASIXc M03 UF3 Fitxers
  Exemple: Llegir fitxer TXT
"""

FILE_NAME= "un_poble.txt"
try:
   f = open(FILE_NAME, mode='rt', encoding='utf-8')
   f.read(2)   # Why 2 ??
   f.read()    # What happens ??
   f.close()
except FileNotFoundError:
   #FileNotFoundError: [Errno 2] No such file or directory: 'LLLL.txt'
   print("Fitxer/Directory no trobat: " + FILE_NAME)