import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'
response = requests.get(url)
r = json.loads(response.text)

for x in r[:5]:
    event = x['type'] + ' :: ' + x['repo']['name']
    print(event)

