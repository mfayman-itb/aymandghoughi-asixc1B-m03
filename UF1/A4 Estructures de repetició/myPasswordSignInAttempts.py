"""
descripción: Modify the IsPasswordOK example so that it acts as GitLab does.
"""
x = 1
PIN = 1234
EASTER_EGG = "0007"

clave = input("Dime la clave: ")
while int(clave) != PIN and clave != EASTER_EGG and x != 3:
    print("Clave incorrecta")
    clave = input("Dime la clave: ")
    x += 1
if x == 3:
    print("Your GitLab account has been locked due to an excessive "
          "amount of unsuccessful sign in attempts. "
          "Your account will automatically unlock in 10 minutes.")
elif int(clave) == PIN:
    print("PIN correcte has fet servir " + str(x) + " intents")
elif clave == EASTER_EGG:
    print("EASTER EGG correcte has fet servir " + str(x) + " intents")
