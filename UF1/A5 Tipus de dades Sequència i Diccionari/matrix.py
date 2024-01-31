MIDA = 4
matrix = [[0] * MIDA for i in range(MIDA)]
print(matrix)    #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for fila in range(MIDA):
   for columna in range(MIDA):
       if fila < columna:
           matrix[fila][columna] = 0
       elif fila > columna:
           matrix[fila][columna] = 2
       else:
           matrix[fila][columna] = 1
for fila in matrix:
   print(' '.join([str(elem) for elem in fila]))

# append() 	Adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
# clear()	Removes all the elements from the list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
# copy()	Returns a copy of the list
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
# count()	Returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
# extend()	Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
# index()	Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
# insert()	Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
# pop()	Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
# remove()	Removes the item with the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
# reverse()	Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
# sort()	Sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()