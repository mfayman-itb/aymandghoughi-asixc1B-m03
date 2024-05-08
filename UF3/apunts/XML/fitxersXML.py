"""
Javier Amaya Boira
ASIXc UF3 A1 XML
13/03/2024
22/04/2024
25/04/2024

source: AEMET
https://www.aemet.es/ca/eltiempo/prediccion/municipios/palafrugell-id17117#detallada
"""

import xml.etree.ElementTree as xml


def leer_xml(nombre_archivo):
   tree = xml.parse(nombre_archivo)
   root = tree.getroot()
   return root


def escribir_xml(root, nombre_archivo):
   tree = xml.ElementTree(root)
   tree.write(nombre_archivo)


def modificar_valor(root, etiqueta, valor):
   for elem in root.iter(etiqueta):
       elem.text = valor


def eliminar_elemento(root, etiqueta):
   for elem in root.findall(etiqueta):
       root.remove(elem)


def agregar_elemento(root, etiqueta, texto):
   new_elem = xml.SubElement(root, etiqueta)
   new_elem.text = texto