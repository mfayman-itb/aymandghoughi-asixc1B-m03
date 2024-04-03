import utils

def calculate_min_grade(grades):
    if not grades:
        return None
    return min(grades)

def calculate_max_grade(grades):
    if not grades:
        return None
    return max(grades)

def mitjana_grades(grades):
    count = len(grades)
    if count == 0:
        return None
    suma = sum(grades)
    mitj = suma / count
    return mitj

def display_result(min_grade, max_grade, mitj):
    if min_grade is None or max_grade is None or mitj is None:
        print("No se ingresaron notas.")
    else:
        print("Nota mínima: ", min_grade)
        print("Nota máxima: ", max_grade)
        print("Mitjana: ", mitj)
