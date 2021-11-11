import requests


#delete a metadata by id
id = 6
url = f"http://localhost:8000/api/metadata/{id}.json"
print(f"Retrieving ALL metadata with id {id} from {url}")
response = requests.delete(url)
print(response.status_code)
print(response.text)