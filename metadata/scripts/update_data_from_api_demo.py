import requests

#UPDATE SCHEMA BY ID
id = 3
data = {"field": "root-element-array-primitive",
        "whitelist": True,
        "cbs": "bnl",
        "data_source": "ga"
    }

url = f"http://localhost:8000/api/schema-field/{id}/"
print(f"updating schema field from {url}")
response = requests.put(url=url,json=data) #PUT for updates
print(response.status_code)
print(response.text)

#UPDATE METADATA BY ID
id = 9
data = {"field": 1,
        "factory": "hash",
        "condition": "I'm making an update",
        "format_in": "",
        "format_out": ""
}

url = f"http://localhost:8000/api/metadata/{id}/"
print(f"updating metadata from {url}")
response = requests.put(url=url,json=data) #PUT for updates
print(response.status_code)
print(response.text)