"""
09/05/2024
Ayman Dghoughi Nouri
ASIXcB
M03 UF3 pp1
Descripció: config del logfile
"""

#region Imports
import os
import logging
#endregion

logFile = os.path.join('.', 'paraules.log')
logFormat = '%(asctime)s - %(levelname)s - %(message)s'
logLevel = logging.DEBUG
logMode = 'at'
color_code = 0
logging.basicConfig(level=logLevel, format=logFormat, filename=logFile, filemode=logMode)

def logger(type, message):
    match type:
        case 'error': logging.error(message)
        case 'info': logging.info(message)
        case 'warning': logging.warning(message)
        case 'debug': logging.debug(message)
        case 'critical': logging.critical(message)