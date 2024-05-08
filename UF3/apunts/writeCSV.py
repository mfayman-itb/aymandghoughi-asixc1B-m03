"""
   JAB Javier Amaya Boira
   ITB Institut Tecnològic de Barcelona
   10/04/2023
   ASIXc M03 UF3 Fitxers
   Exemple: Write CSV File
   SOURCE: https://www.pythontutorial.net/python-basics/python-write-csv-file/
"""
import csv
filename = 'countries.csv'
header = ['name', 'area', 'country_code2', 'country_code3']
data = [
   ['Albania', 28748, 'AL', 'ALB'],
   ['Algeria', 2381741, 'DZ', 'DZA'],
   ['American Samoa', 199, 'AS', 'ASM'],
   ['Andorra', 468, 'AD', 'AND'],
   ['Angola', 1246700, 'AO', 'AGO']
]

with open(filename, 'w', encoding='UTF8', newline='') as f:
   writer = csv.writer(f)
   # write the header
   writer.writerow(header)
   # write multiple rows
   writer.writerows(data)