# line by line output
> file = open("testfile,txt", "r")
> print file.readline():

# read third line only
> file = open("testfile,txt", "r")
> print file.readline(3):

# read lines separately
> file = open("testfile,txt", "r")
> print file.readlines():

# read last line
> last_line = f.readlines()[-1]


# llegeix linia a linia el fitxer present a la ruta passada per parametre i retorna el contingut llegit
def llegirFitxer(rutaFitxer):
    contingut = ""
    fitxerDeText = open(rutaFitxer, mode="r", encoding="utf-8")
    linia = fitxerDeText.readline()
    contingut += linia
    while linia != '':
        linia = fitxerDeText.readline()
        contingut += linia

    fitxerDeText.close()
    return contingut

#main
rutaAlFitxer = input('ruta al fitxero: ')
contingutDelFitxer = llegirFitxer(rutaAlFitxer)
print(contingutDelFitxer)



