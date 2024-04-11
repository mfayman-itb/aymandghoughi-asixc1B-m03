RUTA_ENTRADA = '/home/ayman.dghoughi.7e7/Escriptori/DADES/ayman/M3/UF3/A1 Fonaments de gestió de Ditxers/Dragon.in'
RUTA_SALIDA = '/home/ayman.dghoughi.7e7/Escriptori/DADES/ayman/M3/UF3/A1 Fonaments de gestió de Ditxers/DragonEyesClosed.out'

def cambiarOjos(linea):
    nueva_linea = linea.replace("0 \ 0", "👁\👁")
    return nueva_linea

def leerYGuardarArchivo():
    with open(RUTA_ENTRADA, mode="r", encoding="utf-8") as archivo_entrada:
        with open(RUTA_SALIDA, mode="w", encoding="utf-8") as archivo_salida:
            for linea in archivo_entrada:
                nueva_linea = cambiarOjos(linea)
                archivo_salida.write(nueva_linea)

leerYGuardarArchivo()


