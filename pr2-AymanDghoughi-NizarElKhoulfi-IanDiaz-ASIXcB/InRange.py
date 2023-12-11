'''
Ayman Dghoughi, Nizar El Khoulfi, Ian Diaz
11/10/23
ASIXc M03 UF1 A2
Descripció: Programa que mostra True si el cinquè valor, està comprès dins els dos rangs
'''

try:
    valors = list(map(int, input("Introdüeix 5 valors separats per un espai...\n").split(" ")))

    if valors[4] in range(valors[0], valors[1]) and range(valors[2], valors[3]):
        print("True")
    else:
        print("False")

except Exception as e:
    print(e)
    exit(1)