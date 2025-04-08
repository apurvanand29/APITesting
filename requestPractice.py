import requests
import json

# 200 success | 201 creater | 204 no content
# 400 bad request | 401 unauthorized | 403 forbidden | 404 not found
# 500 internal server error

# Making a GET request
url = 'https://jsonplaceholder.typicode.com/posts/1'
request = requests.get(url=url,)
jsonres = request.json()
print(type(request))
print(request.status_code)
print(jsonres['id'])
print(jsonres['title'])