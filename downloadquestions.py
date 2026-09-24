import requests
url="https://opentdb.com/api.php?amount=50"
response=requests.get(url)
print(response.status_code)
print(response.json)

