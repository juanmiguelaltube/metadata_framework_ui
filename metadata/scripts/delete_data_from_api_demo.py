import requests


#DELETE METADATA BY ID
id = 9
url = f"http://localhost:8000/api/metadata/{id}/"
print(f"deleting a metadata with id {id} from {url}")
response = requests.delete(url)
print(response.status_code)
print(response.text)

#DELETE SCHEMA FIELD BY ID
id = 3
url = f"http://localhost:8000/api/schema-field/{id}/"
print(f"deleting a schema field with id {id} from {url}")
response = requests.delete(url)
print(response.status_code)
print(response.text)