try:
    num1 = int(input())
    num = num1
    count = 0
    if num == 1 or num == 0:
        print(f"El número {num1} té 1 dígit.")
        pass
    else:
        if num < 0:
            num *= -1
        while num > 1:
            num = num / 10
            count += 1
        print(f"El número {num1} té {count} dígits.")
except Exception as e:
    if ValueError:
        print("Siusplau, introdueix només nombres enters.")
    print(e)