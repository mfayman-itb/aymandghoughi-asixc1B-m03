import statistics
def calcMitjana():
    nums = input("Introduce una lista de números separados por espacios: ").split()
    nums = [int(num) for num in nums]

    return statistics.mean(nums)

def calcMediana():
    nums = input("Introduce una lista de números separados por espacios: ").split()
    nums = [int(num) for num in nums]

    return statistics.median(nums)

def calcDesv():
    nums = input("Introduce una lista de números separados por espacios: ").split()
    nums = [int(num) for num in nums]

    return statistics.pstdev(nums)

