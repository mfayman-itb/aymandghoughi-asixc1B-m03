"""
descripción: tu billete es valido o no
"""
num = int(input("Give me a valid bill: "))

if num == 5 or 10 or 20 or 50 or 100 or 200 or 500:
    print("valid bill")
else:
    print("invalid bill")
