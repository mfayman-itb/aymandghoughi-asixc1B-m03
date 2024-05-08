"""
Description: programa que llegint el fitxer CSV del Bicing  de Barcelona ens doni la següent informació:
--> Obtenir la "capacity" de l'estació amb més bicicletes i la que en te menys     estació: 13 amb 54 i 505 amb 0
--> Obtenir la "capacity" total de la ciutat de Barcelona  13605 Bicicletes i 506 Estacions amb id fins 519

Usage:
Input --> CSV file '2023_03_Marc_BicingNou_INFORMACIO.csv.7z'
Output --> Terminal
"""

import csv

csvF = '2023_03_Marc_BicingNou_INFORMACIO.csv'
allCapacity = []
IDList = []

def get_csv():
    with open(csvF, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['station_id'] not in IDList:
                IDList.append(row['station_id'])
                allCapacity.append(int(row['capacity']))
        print(allCapacity)

def main():
    get_csv()
    print('max =', {str(max(allCapacity))})
    print('min =', {str(min(allCapacity))})
    print('total stations bicilones', {str(sum(allCapacity))})

if __name__ == "__main__":
    main()
