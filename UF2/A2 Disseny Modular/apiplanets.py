import requests
YOUR_API_KEY = 'eVIoA414OY2Ik/Dofu386g==W8gO3uOfARfFPKoj'

name = 'Pluto'
api_url = 'https://api.api-ninjas.com/v1/planets?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': YOUR_API_KEY})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)