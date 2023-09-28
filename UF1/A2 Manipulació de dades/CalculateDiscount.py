original = float(input("original price: "))
actual = float(input("actual price: "))
discount = ((original - actual) / original) * 100
print(discount, "%")