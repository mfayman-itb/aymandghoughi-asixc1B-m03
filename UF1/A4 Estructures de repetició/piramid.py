num = int(input("Give me a number: "))
obj = "🧱"

for i in range(1, num + 1):
    print(obj * i, end=" ")
    if i < num:
        print()