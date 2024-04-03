#Importar un mòdul import
import random
print(random.randint(1, 10))
#assignar-lo a un nom diferent
import random as rdm
print(rdm.randint(1, 10))

#Importar una funció
from math import sin
sin(1) #0.8414709848078965

#Importar tots els noms d'un mòdul
from module_name import *

Per exemple
from math import *
sqrt(2)   # instead of math.sqrt(2)
ceil(2.7) # instead of math.ceil(2.7)