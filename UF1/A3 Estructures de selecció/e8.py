"""
descripción: te aceptan  o no dependiendo de unas condiciones
"""
nums = input("Introdueix la teva nota, la teva edat i si ets M/F: ").upper().split()

if nums[0] >= "5" and nums[1] >= "18" and nums[2] == "F":
    print("Acceptada")
elif nums[0] >= "5" and nums[1] >= "18" and nums[2] == "M":
    print("Possible")
else:
    print("No Acceptada")