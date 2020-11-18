import json
import requests
import pandas as pd

api_token = ''
api_url_base = 'https://api.deezer.com/artist/1/top'
res = requests.get('https://api.deezer.com/artist/1/top')

if res:
    print('Response OK')
else:
    print('Response Failed')

#print(res.headers)
# print(res.text)

# print(json)

response_json = (res.text)
loaded_json = json.loads(response_json)

# print(loaded_json)

tracks = loaded_json['data']

# print(tracks)

print("\nTOP 5 Artist's tracks")
for track in tracks:
    print(track["id"])
