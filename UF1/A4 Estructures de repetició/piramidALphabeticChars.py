"""
descripción: A cada linia apareix un carcater i la seguent linia apareix un carcater més de forma progresiva. Fins aconseguir tenir una linia que mostri de la A fins la Z
"""
START = ord('A')
END = ord('Z')
for i in range(START, END + 1):
    for j in range(START, i + 1):
        print(chr(j), end=" ")
    print()
