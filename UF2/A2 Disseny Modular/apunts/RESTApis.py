#pip install requests
import requests
response = requests.get("https://www.itb.cat/")
print(response.text)