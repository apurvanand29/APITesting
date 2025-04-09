import requests
import json

# Making a GET request
url1 = 'https://httpbin.org/get'
response = requests.get(url=url1)
assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
jsonObject = response.json()
print(jsonObject['origin'])
host = jsonObject['headers']['Host']
expHost = 'httpbin.org'
assert host == expHost, f"Expected host '{expHost}', but got {host}"