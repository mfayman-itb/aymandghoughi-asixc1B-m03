"""
descripción: dice cual es mas grande
"""
num = input("Give me two nbrs: ").split()

if num[0] > num[1]:
    print(num[0])
elif num[0] == num[1]:
    print("Equal numbers")
else:
    print(num[1])