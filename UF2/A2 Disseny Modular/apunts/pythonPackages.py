#DATETIME
from datetime import *
ara = datetime.now()
print(ara)

#REQUESTS
import requests
r = requests.get('https://api.spotify.com/')
r.status_code

print(r.headers)
print(r.encoding)