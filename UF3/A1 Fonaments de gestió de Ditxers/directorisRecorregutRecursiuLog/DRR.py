"""
Javier amaya Boira
ASIXc UF3 A1 Exemple
08/04/2024

Recorregut d'un arbre de directoris.
Algoritme recursiu.
Demana a l'usuari des de quin directori es vol començar a fer el recorregut

us.path.join()
Genera rutes d'arxius i directoris que són vàlides en qualsevol sistema operatiu.
Això assegura que el programa funcioni correctament en Windows, Linux i macOS sense necessitat de modificacions addicionals.
"""
import logging
import os
import signal
import time

logFile = 'recorregut.log'
logFormat = '[%(asctime)s] [%(levelname)s] %(message)s'
logLevel = logging.DEBUG
logMode = 'at'

logging.basicConfig(level=logLevel,format=logFormat,filename=logFile,filemode=logMode)

start = time.time()
logging.info('Program initialized')

def sigint(sig, frame):
    end = time.time()
    laps = end-start
    logging.info('Program ended due to SIGINT, done in %.3f', laps)
    exit(0)
signal.signal(signal.SIGINT, sigint)
def recorrer_arbol_directorios(directorio):
    try:
       # Obtener la lista de archivos y directorios en el directorio actual
       contenido = os.listdir(directorio)

       # Recorrer cada elemento del directorio actual
       for elemento in contenido:
           # Crear la ruta completa del elemento
           ruta_elemento = os.path.join(directorio, elemento)

           # Si el elemento es un directorio, recorrer recursivamente
           if os.path.isdir(ruta_elemento):
               print("Directorio:", ruta_elemento)
               recorrer_arbol_directorios(ruta_elemento)
           else:
               print("Archivo:", ruta_elemento)
    except Exception as e:
        logging.error(f"{directorio}: {str(e)}")


# Función principal
def main():
   # Solicitar al usuario el directorio inicial
   directorio_inicial = input("Introduce la ruta del directorio inicial: ")

   # Verificar si el directorio ingresado existe
   if not os.path.isdir(directorio_inicial):
       print("El directorio especificado no existe.")
       logging.error('Directory not found')
   else:
       # Llamar a la función recursiva para recorrer el árbol de directorios
       print("\nRecorrido del árbol de directorios:")
       recorrer_arbol_directorios(directorio_inicial)

start = time.time()

if __name__ == "__main__":
    main()

end = time.time()
laps = end-start
logging.info('Program ending, done in %.3f seconds', laps)
