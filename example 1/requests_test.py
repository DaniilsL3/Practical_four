import requests


# Test GET request with parameters (headers, timeout, allow redirect).

url = 'https://jsonplaceholder.typicode.com/posts'
headers = {'Accept': 'application/json'}
timeout = 10
allow_redirects = True

response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=allow_redirects)
print(response.text)


# POST request with data, headers, and verify parameters.

url = 'https://jsonplaceholder.typicode.com/posts'
data = {'title': 'example', 'body': 'Hello World', 'userId': 1}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
verify = True

response = requests.post(url, data=data, headers=headers, verify=verify)
print(response.text)


# PUT request with json, headers and timeout parameters.

url = 'https://jsonplaceholder.typicode.com/posts/1'
json_data = {'title': 'Updated Title', 'body': 'Updated Content', 'userId': 1}
headers = {'Content-Type': 'application/json'}
timeout = 5

response = requests.put(url, json=json_data, headers=headers, timeout=timeout)
print(response.text)


# DELETE request with auth and timeout.

url = 'https://jsonplaceholder.typicode.com/posts/1'
auth = ('username', 'password')
timeout = 5

response = requests.delete(url, auth=auth, timeout=timeout)
print(response.status_code)


# HEAD request with allow redirects and cookies.

url = 'https://jsonplaceholder.typicode.com/posts'
cookies = {'session_id': '12345'}
allow_redirects = False

response = requests.head(url, cookies=cookies, allow_redirects=allow_redirects)
print(response.headers)


# OPTIONS request with SSL verification.

url = 'https://jsonplaceholder.typicode.com/posts'
verify = False  # Caution: Disables SSL certificate verification

response = requests.options(url, verify=verify)
print(response.headers)


# PATCH request with json and headers.

url = 'https://jsonplaceholder.typicode.com/posts/1'
json_data = {'title': 'Patched Title'}
headers = {'Content-Type': 'application/json'}

response = requests.patch(url, json=json_data, headers=headers)
print(response.text)


