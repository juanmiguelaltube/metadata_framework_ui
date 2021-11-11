import requests


#DELETE METADATA BY ID
id = 1
url = f"http://localhost:8000/api/metadata/{id}/"
print(f"Retrieving ALL metadata with id {id} from {url}")
response = requests.delete(url)
print(response.status_code)
print(response.text)