import csv

csvF = '2023_03_Marc_BicingNou_INFORMACIO.csv'
allCapacity = []
IDList = []

def get_csv():
    with open(csvF, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['station_id'] not in IDList:
                IDList.append(row['station_id'])
                allCapacity.append(int(row['capacity']))
        print(allCapacity)

def main():
    get_csv()
    print('max =', {str(max(allCapacity))})
    print('min =', {str(min(allCapacity))})
    print('total stations bicilones', {str(sum(allCapacity))})

if __name__ == "__main__":
    main()
