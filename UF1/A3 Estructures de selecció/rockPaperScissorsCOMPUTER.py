num = int(input("Piedra, papel o tijeras, un, dos ,tres ya! "))
import random

aleatorio = int(random.uniform(1, 4))
rock = 1
paper = 2
scissor = 3

if num == rock and aleatorio == paper:
    print("The second one wins")
elif num == rock and aleatorio == scissor:
    print("The first onw wins")
elif num == paper and aleatorio == scissor:
    print("The second wins")
elif num == aleatorio:
    print("Equals")

print("COMPUTER choiced " + str(aleatorio))