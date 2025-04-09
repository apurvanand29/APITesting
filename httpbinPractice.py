import requests
import json

# Making a GET request
url = 'https://httpbin.org/get'
response = requests.get(url=url)