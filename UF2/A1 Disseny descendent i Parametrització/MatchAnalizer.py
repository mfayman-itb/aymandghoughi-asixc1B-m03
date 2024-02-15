#region Functions
teams = []
points = []

def what_teams():
    t1 = input('local team: ')
    t2 = input('visitor team: ')
    return t1,t2
def obtain_points():
    scores = []
    while True:
        oldscores = scores
        scores = input("Introduce the result (or -1 to finish): ").split()
        if '-1' in scores:
            break
        if len(scores) != 2:
            print("Please enter exactly 2 scores separated by space.")
            continue
        if not all(score.isdigit() for score in scores):
            print("Please enter only integers.")
            continue
        points.append((int(scores[0]), int(scores[1])))
    return points
print(points)
def compare_points(points):
        for score in points:
            if score[0] == 1:
                print("Cistella de", teams[0])
            elif score[0] == 2:
                print("Doble de", teams[0])
            elif score[0] == 3:
                print("Triple de", teams[0])
            else:
                print("Tir lliure de", teams[0])

            if score[1] == 1:
                print("Cistella de", teams[1])
            elif score[1] == 2:
                print("Doble de", teams[1])
            elif score[1] == 3:
                print("Triple de", teams[1])
            else:
                print("Tir lliure de", teams[1])
def winner():
    score_team_1 = sum([score[0] for score in points])
    score_team_2 = sum([score[1] for score in points])
    
    if score_team_1 > score_team_2:
        print("Guanya", teams[0])
    elif score_team_2 > score_team_1:
        print("Guanya", teams[1])
    else:
        print("Empat")
#endregion

#region Main
t1, t2 = what_teams()
teams.append(t1)
teams.append(t2)
obtain_points()
compare_points(points)
winner()
#endregion
