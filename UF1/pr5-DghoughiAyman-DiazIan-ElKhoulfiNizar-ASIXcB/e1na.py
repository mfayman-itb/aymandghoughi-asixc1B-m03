try:
    n1 = int(input())
    n2 = int(input())

    if n1 < n2:
        for i in range(n1, n2 + 1):
            if i % n1 == 0 and i <= n2:
                print(i, end=" ")
    else:
        print("El primer número té que ser més gran que el segon")
except Exception as e:
    print(e)
