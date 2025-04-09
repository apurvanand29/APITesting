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
code = request.status_code
try:
 assert code ==200
 print("✅ Status code is 200 - Test 1 Passed!")
except AssertionError:
    print(f"❌ Status code was {code} - Test 1 Failed.")
print(jsonres['id'])
print(jsonres['title'])

# Making a GET request to find matching id by iterating through the list
url1 = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url=url1)
code = response.status_code
try:
    assert code == 200
    print("✅ Status code is 200 - Test 2 Passed!")
except AssertionError:
    print(f"❌ Status code was {code} - Test 2 Failed.")

list = response.json()
for i in range(0, len(list)):
    if list[i]['id'] == 10:
        id = list[i]['id']
        if id==int(10):
            title = list[i]['title']
assert title == 'optio molestias id quia eum', f"Actual title does not match expected title '{title}'"
print(f"Title for id {id} is: {title}")
    