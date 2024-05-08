"""
Description: programa que a partir del fitxer XML, calculi, i mostri per pantalla:
--> Probabilitat de precipitació
--> Temperatura mitjana

Usage:
Input --> CSV file '2023_03_Marc_BicingNou_INFORMACIO.csv.7z'
Output --> Terminal
"""

import xml.etree.ElementTree as xeet

weatherF = 'localidad_17202.xml'

def readXML():
    tree = xeet.parse(weatherF)
    root = tree.getroot()
    return root

def get_precipitation():
    tree = readXML()
    prediccion = tree.find(".//prediccion")
    dias = prediccion.findall(".//dia")

    for dia in dias:
        fecha = dia.get("fecha")
        prob_precipitacion = dia.find(".//prob_precipitacion[@periodo='00-24']")

        if prob_precipitacion is not None:
            precipitation_percentage = prob_precipitacion.text
            print(f"On {fecha}, precipitation percentage: {precipitation_percentage}%")

            temperaturas = dia.findall(".//temperatura/dato")
            temperatures = [int(temperatura.text) for temperatura in temperaturas]
            if temperatures:
                avg_temperature = sum(temperatures) / len(temperatures)
                print(f"Average temperature: {avg_temperature}°C\n")
            else:
                print("No temperature data available for this day\n")

get_precipitation()