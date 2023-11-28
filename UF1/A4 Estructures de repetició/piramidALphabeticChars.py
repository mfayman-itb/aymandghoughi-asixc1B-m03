START = ord('A')
END = ord('Z')
for i in range(START, END + 1):
    for j in range(START, i + 1):
        print(chr(j), end=" ")
    print()
