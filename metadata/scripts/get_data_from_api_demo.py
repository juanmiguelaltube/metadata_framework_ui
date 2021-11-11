import requests


url = "http://localhost:8000/api/metadata.json"
print(f"calling {url}")
response = requests.get(url)
print(response.status_code)
print(response.text)
