#region Functions
def teams():
    team1 = input()
    team2 = input()

def points():
    points = []
    while points != '-1':
        if len(points) == 2:
            points = input().split()
        else:
            print("Introdueix 2 numeros")


#endregion
teams()
points()