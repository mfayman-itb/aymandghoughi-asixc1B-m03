"""
Description: programa que llegint el fitxer JSON de les platges de Barcelona ens doni la següent informació:
--> Obtenir els noms de tots els districtes de Barcelona que tenen platges CV? i SM?
--> Obtenir la quantitat de platges que hi ha al districte de "Ciutat Vella"  4?

Usage:
Input --> JSON file 'opendatabcn_NP-NASIA_Platges-js'
Output --> Terminal
"""

import json
import os.path

jsonF = os.path.join('.', 'opendatabcn_NP-NASIA_Platges-js.json')

def get_json_file():
    with open(jsonF, 'r') as f:
        x = json.load(f)
    return x

def get_districts(x):
    district = []
    for d in x:
        district.append(d['addresses'][0]['district_name'])
    print(set(district))

def get_playa(x):
    count = 0
    for i in x:
        if i['addresses'][0]['district_name'] == 'Ciutat Vella':
            count += 1
    print(count)

def main():
    x = get_json_file()
    get_districts(x)
    get_playa(x)

if __name__ == "__main__":
    main()