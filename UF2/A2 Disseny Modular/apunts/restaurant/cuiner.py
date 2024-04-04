import pinche

def mostrarIngredients(ingredients):
   for i in ingredients:
       print(i)

def ferTruita():
   print("CUINER: Estic fent truita")
   ingredients=pinche.comprarIngredientsTruita()
   mostrarIngredients(ingredients)

def ferMacarrons():
   print("CUINER: Estic fent MAcarrons")
   ingredients=pinche.comprarIngredientsMacarrons()
   mostrarIngredients(ingredients)