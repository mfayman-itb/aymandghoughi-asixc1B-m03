"""
   JAB Javier Amaya Boira
   ITB Institut Tecnològic de Barcelona
   13/03/2023
   ASIXc M03 UF3 Fitxers
   Exemple: Python logging best practices
   SOURCE:
       https://www.w3resource.com/python-exercises/modules/python-module-csv-exercise-1.php
       https://coralogix.com/blog/python-logging-best-practices-tips/
"""

import logging

logFile = 'myapp.log'
logFormat='%(asctime)s %(levelname)s %(message)s'
logLevel= logging.DEBUG
logMode = 'w'

logging.basicConfig(level=logLevel,format=logFormat,filename=logFile,filemode=logMode)


logging.debug("Debug message")
logging.info("Informative message")
logging.error("Error message")
logging.warning('Protocol problem: %s', 'connection reset')