"""
Propósito:  Solicita al usuario un valor, generalmente una contraseña, sin repetir lo que escribe en la consola.
           Contraseña sin mostrar lo que escribe el usuario la pantalla.
           El módulo getpass proporciona una forma portátil de manejar tales
         solicitudes de contraseña de forma segura.
IMPORTANTE: Se ha de ejecutar en TERMINAL

"""
import getpass # getpass — Solicitar contraseña de forma segura

try:
   p = getpass.getpass() # getpass.getpass('Introduce tu contraseña: ') # Introduce tu contraseña:
except Exception as err:
   print('ERROR:', err)
else:
   print('You entered:', p)