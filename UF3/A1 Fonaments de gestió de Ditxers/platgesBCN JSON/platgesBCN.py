import json

jsonF = 'opendatabcn_NP-NASIA_Platges-js.json'

def get_json_file():
    with open(jsonF, 'r') as f:
        x = json.load(f)
    return x

def get_districts(x):
    district = []
    for d in x:
        district.append(d['addresses'][0]['district_name'])
    print(set(district))

def get_playa(x):
    count = 0
    for i in x:
        if i['addresses'][0]['district_name'] == 'Ciutat Vella':
            count += 1
    print(count)

def main():
    x = get_json_file()
    get_districts(x)
    get_playa(x)

if __name__ == "__main__":
    main()