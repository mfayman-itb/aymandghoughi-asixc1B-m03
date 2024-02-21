"""
Ayman Dghoughi Nouri
01/02/2024
pp3
Descrició: Programa que mostra una frase encriptada.
"""
try:
    ABC = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'ñ':14,
           'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'w':22,'v':23,'x':24,'y':25,'z':0}
    paraula = input().lower()
    i = 0
    print(paraula[i])
    print(ABC[a])
    count = 0
    for i in paraula:
        if paraula[i] == ABC[i]:
            paraula[i] == ABC[i]
    print(paraula)
except Exception as e:
    print(e)
