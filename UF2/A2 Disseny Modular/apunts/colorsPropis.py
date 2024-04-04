# Class of different styles --------------------------------------------------------------------------------

class myColors():
   BLACK = '\033[30m'
   RED = '\033[31m'
   GREEN = '\033[32m'
   YELLOW = '\033[33m'
   BLUE = '\033[34m'
   MAGENTA = '\033[35m'
   CYAN = '\033[36m'
   WHITE = '\033[37m'
   UNDERLINE = '\033[4m'
   RESET = '\033[0m'

print(myColors.YELLOW + "Hello, World!")
print(myColors.UNDERLINE + "Hello, World!")
print(myColors.BLUE + "Hello, World!")