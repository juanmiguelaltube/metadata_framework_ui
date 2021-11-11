import requests


#UPDATE METADATA BY ID
id = 3
data = {"field": 1,
        "factory": "hash",
        "condition": "I'm making an update",
        "format_in": "",
        "format_out": ""
}

url = f"http://localhost:8000/api/metadata/{id}/"
print(f"creating new metadata from {url}")
response = requests.put(url=url,json=data) #PUT for updates
print(response.status_code)
print(response.text)