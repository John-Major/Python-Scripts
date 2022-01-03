import requests
import json

test = 'https://api.polygon.io/v1/meta/symbols/AAPL/company?apiKey=MNExhabeDDgHYLqKlxDoT79JUdvT_OaI'

response = requests.get(test)
json_response = response.json()
print(json_response['logo'])
input('Press any key to continue...')
