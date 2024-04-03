"""
Ayman Dghoughi Nouri
01/02/2024
pp3
Descrició: Programa que calcula la paraula més llarga, la més curta i la mida mitjana de les paraules incloses. El programa para quan s'introdueix '\q'
"""
try:
    lst = input().split()
    i = 0
    while i < len(lst) and lst[i] != '\q':
        i += 1
    lst.remove('-1')
    print(lst)
    for i in lst:
        if len(lst[i]) > len(lst[i + 1]):
            max = lst[i]
        elif len(lst[i]) > len(lst[i + 1]):
            min = i
        else:
            print("igual")
except Exception as e:
    print(e)
