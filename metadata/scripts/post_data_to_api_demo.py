import requests


url = "http://localhost:8000/api/metadata.json"
print(f"Retrieving ALL metadata from {url}")
response = requests.get(url)
print(response.status_code)
print(response.text)


id = 7
url = f"http://localhost:8000/api/metadata/{id}.json"
print(f"Retrieving ALL metadata with id {id} from {url}")
response = requests.get(url)
print(response.status_code)
print(response.text)