import analizer
teams = []
points = []

def what_teams():
    t1 = input('local team: ')
    t2 = input('visitor team: ')
    return t1,t2

def main():
    t1, t2 = what_teams()
    teams.append(t1)
    teams.append(t2)
    analizer.obtain_points()
    analizer.compare_points(points)
    analizer.winner()

if __name__ == "__main__":
    main()