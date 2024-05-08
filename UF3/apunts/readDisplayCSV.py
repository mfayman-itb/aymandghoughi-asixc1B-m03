"""
   JAB Javier Amaya Boira
   ITB Institut Tecnològic de Barcelona
   13/03/2023
 10/04/2023
   ASIXc M03 UF3 Fitxers
   Exemple:Read and display the content of a given CSV file.
           Use csv.reader
   SOURCE: https://www.w3resource.com/python-exercises/modules/python-module-csv-exercise-1.php
"""
import csv
FILE_NAME="employees.csv"
try:
   reader = csv.reader(open(FILE_NAME))
   for row in reader:
       print(row)
except FileNotFoundError:
   #FileNotFoundError: [Errno 2] No such file or directory: 'employees.csv'
   print(f"Fitxer/Directory no trobat: { FILE_NAME}")


#A slightly more advanced use of the reader — catching and reporting errors:
import csv, sys
filename = 'some.csv'
try:
   with open(filename, newline='') as f:
       reader = csv.reader(f)

       for row in reader:
           print(row)
except csv.Error as e:
   sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
except FileNotFoundError:
   print(f"Fitxer/Directory no trobat: {filename}")