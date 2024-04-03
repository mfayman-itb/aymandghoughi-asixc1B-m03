import calculus
import utils

def main():
    grades = utils.grade_input()
    min_grade = calculus.calculate_min_grade(grades)
    max_grade = calculus.calculate_max_grade(grades)
    mitj = calculus.mitjana_grades(grades)
    calculus.display_result(min_grade, max_grade, mitj)

if __name__ == "__main__":
    main()