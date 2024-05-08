"""
Description: programa que analitzi els resultats d'un partit de bàsquet. L'usuari introduirà la ruta al fitxer.

Usage:
Input --> File
Output --> File
"""

import os

inputFile = os.path.join('.', 'resultats')
outputFile = os.path.join('.', 'resultats_output.txt')

# Para que el user me de la ruta (no hace falta para que funcione)
def get_input_path():
    while True:
        input_path = input("Please enter the path of the input file: ")
        if os.path.exists(input_path):
            return input_path
        else:
            print("File not found. Please enter a valid path.")

def compare_scores(current_score, previous_score, teams, results):
    difference = (current_score[0] - previous_score[0], current_score[1] - previous_score[1])
    if difference[0] == 0 and difference[1] in [1, 2, 3]:
        results.append(f"{teams[1]} scores a basket")
    elif difference[1] == 0 and difference[0] in [1, 2, 3]:
        results.append(f"{teams[0]} scores a basket")
    elif difference[0] == 0 and difference[1] == 1:
        results.append(f"{teams[1]} makes a free throw")
    elif difference[0] == 0 and difference[1] == 3:
        results.append(f"{teams[1]} scores a three-pointer")
    elif difference[0] == 1 and difference[1] == 0:
        results.append(f"{teams[0]} makes a free throw")
    elif difference[0] == 3 and difference[1] == 0:
        results.append(f"{teams[0]} scores a three-pointer")

def get_teams(path):
    try:
        with open(path, 'r') as file:
            team1 = file.readline().strip()
            team2 = file.readline().strip()
        return team1, team2
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None, None

def generate_results(input_path, output_path):
    if not os.path.exists(outputFile):
        os.mkdir(os.path.join('', 'output'))
    team1, team2 = get_teams(input_path)
    if team1 and team2:
        results = []
        previous_score = (0, 0)
        with open(input_path, 'r') as file:
            next(file) # Skip the first two lines
            next(file)
            for line in file:
                current_score = tuple(map(int, line.strip().split()))
                if current_score == (-1, -1):
                    break
                compare_scores(current_score, previous_score, (team1, team2), results)
                previous_score = current_score

        winner = team1 if previous_score[0] > previous_score[1] else team2
        results.append(f"{winner} wins")

        try:
            with open(output_path, 'w') as output_file:
                for result in results:
                    output_file.write(result + '\n')
            print(f"Results saved to '{output_path}'")
        except Exception as e:
            print(f"Error writing to output file: {e}")

def main():
    #input_file = get_input_path()
    #output_file = os.path.join('.', 'results_output.txt')
    generate_results(inputFile, outputFile)

if __name__ == '__main__':
    main()

