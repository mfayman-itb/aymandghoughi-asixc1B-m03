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
def compare_points():

def winner():

#endregion
what_teams()
obtain_points()
