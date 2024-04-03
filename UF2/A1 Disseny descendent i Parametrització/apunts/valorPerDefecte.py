#EXPLICACION VALOR POR DEFECTO
def operar(n1, n2, operador='+', resposta='El resultat és '):
   resultat= resposta
   if operador=="+":
       resultat= resultat + str(n1+n2)
   elif operador=="-":
       resultat= resultat + str(n1-n2)
   else:
       resultat= resultat +  "BACALAOOOOOOO"
   return resultat

print(operar(5,7))                                          #'El resultado es 12'
print(operar(5,7,"-"))                              #'El resultado es -2'
print(operar(5,7,"-","La resta es "))       #'La resta es -2'
print(operar(5,7,"/"))                              # El resultat és BACALAOOOOOOO



#EXPLICACION KEYWORDS
print("Keyword")
print(operar(5,7))         # dos paràmetres posicionals
print(operar(n1=4,n2=6))   # dos parámetros keyword
print(operar(n2=6,n1=4))  # al fer servir el NOM es poden CANVIAR de LLOC


print(operar(4,6,resposta="La suma és: "))    		        # dos paràmetres posicionals i uno keyword
print(operar(4,6,resposta="La resta és: ",operador="-"))    # dos paràmetres posicionals i dos keyword