import json
import requests

pyyntö ='https://api.chucknorris.io/jokes/random'

vastaus = requests.get(pyyntö)
json_vastaus = vastaus.json()
#print(json.dumps(json_vastaus, indent=2))

print('Chuck Norris approves of this message:'
      f'\n{json_vastaus["value"].capitalize()}')