num = input("give me a numer from 1 to 3: ").split()

rock = str(1)
paper = str(2)
scissor = str(3)

if num[0] == rock and num[1] == paper:
    print("The second one wins")
elif num[0] == rock and num[1] == scissor:
    print("The first onw wins")
elif num[0] == paper and num[1] == scissor:
    print("The second wins")
elif num[0] == num[1]:
    print("Equals")
