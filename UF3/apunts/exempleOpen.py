"""
  JAB Javier Amaya Boira
  ITB Institut Tecnològic de Barcelona
  14/03/2023
  29/03/2023
  ASIXc M03 UF3 Fitxers
  Exemple: Escriure fitxer TXT
"""

FILE_NAME="un_poble.txt"
try:
   f = open(FILE_NAME, mode='wt', encoding='utf-8')
   resultat=f.write('La mare era mestra.\n')
   print(resultat) #Què és "resultat?
   resultat=f.write('Vivíem tots dos sols. No teníem ni vàter.\nDamunt de la casa, les estrelles')
   print(resultat) #Què és "resultat?
   f.close()
except FileNotFoundError:
   #FileNotFoundError: [Errno 2] No such file or directory: 'un_poble.txt'
   print("Fitxer/Directory no trobat: " + FILE_NAME)