import obtenirPreu

def main():
    preus = obtenirPreu.obtenir_preus()
    preu_mes_baix = obtenirPreu.trobar_preu_mes_baix(preus)
    obtenirPreu.mostrar_preu_mes_baix(preu_mes_baix)

if __name__ == "__main__":
    main()