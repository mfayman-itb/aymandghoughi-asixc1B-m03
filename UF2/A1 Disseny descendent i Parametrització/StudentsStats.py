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
    mitj_grade = suma / count
    return mitj_grade

def display_result(min_grade, max_grade, mitj_grade):
    if min_grade is None or max_grade is None or mitj_grade is None:
        print("No se ingresaron notas.")
    else:
        print("Nota mínima: ", min_grade)
        print("Nota máxima: ", max_grade)
        print("Mitjana: ", mitj_grade)
def main():
    grades = grade_input()
    min_grade = calculate_min_grade(grades)
    max_grade = calculate_max_grade(grades)
    mitj_grade = mitjana_grades(grades)
    display_result(min_grade, max_grade, mitj_grade)

if __name__ == "__main__":
    main()