"""
Javier Amaya Boira
ASIXc UF3 A1 XML
13/03/2024
22/04/2024


source: AEMET
https://www.aemet.es/ca/eltiempo/prediccion/municipios/palafrugell-id17117#detallada
"""
import fitxersXML as dades

archivo_xml = "localidad_17117.xml"
def main():
   try:
       # Leer el archivo XML
       root = dades.leer_xml(archivo_xml)

       # Modificar un valor
       dades.modificar_valor(root, "maxima", "20")

       # Eliminar un elemento
       #dades.eliminar_elemento(root, "./prediccion/dia[@fecha='2024-03-14']/prob_precipitacion[@periodo='00-12']")

       # Agregar un elemento
       dades.agregar_elemento(root.find("./prediccion/dia[@fecha='2024-03-13']"), "nuevo_elemento", "Nuevo texto")

       # Escribir los cambios en el archivo XML
       dades.escribir_xml(root, "localidad_17117_Modificat.xml")

       print("Operaciones realizadas con éxito.")
   except:
       print("Error al realizar las operaciones.")

if __name__ == "__main__":

   main()

