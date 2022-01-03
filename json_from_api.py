import requests
import json

test = 'api key + website'

response = requests.get(test)
json_response = response.json()
print(json_response['logo'])
input('Press any key to continue...')
