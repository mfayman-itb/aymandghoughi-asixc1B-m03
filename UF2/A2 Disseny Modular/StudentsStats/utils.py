def grade_input():
    grades = []
    input_list = input().split()
    for grade in input_list:
        if grade == '-1':
            break
        try:
            grade = float(grade)
            if 0 <= grade <= 10:
                grades.append(grade)
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Por favor, ingrese una nota válida.")
    return grades