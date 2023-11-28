num = int(input())
ye = ""

while(num > 0 and num <= 256):
    damn = num % 2
    ye = str(damn) + ye
    num = num // 2
print(ye)
