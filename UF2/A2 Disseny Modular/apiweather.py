import requests
YOUR_API_KEY = 'eVIoA414OY2Ik/Dofu386g==W8gO3uOfARfFPKoj'

city = 'miami'
api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
response = requests.get(api_url, headers={'X-Api-Key': YOUR_API_KEY})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)