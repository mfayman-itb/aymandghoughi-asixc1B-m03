hour = input("Give the hour: ").split()
h = hour[0]
m = hour[1]

if int(hour[1]) == 59:
    h = int(hour[0]) + 1
    if hour[0] == 23:
        hour[0] = "00"
    hour[1] = "00"
if int(hour[2]) == 59:
    m = int(hour[1]) + 1
    hour[2] = "00"
print(h, ":", m, ":", hour[2])
