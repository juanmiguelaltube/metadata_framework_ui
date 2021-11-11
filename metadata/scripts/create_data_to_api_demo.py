import requests

#CREATE SCHEMA FIELD 
data =  {"field": "root-element-array-primitive",
        "whitelist": True,
        "cbs": "bnl",
        "data_source": "ga"
    }

url = "http://localhost:8000/api/schema-field/"
print(f"creating new schema field from {url}")
response = requests.post(url=url,json=data) #POST for creation
print(response.status_code)
print(response.text)


#CREATE METADATA 
data = {"field": 1,
        "factory": "hash",
        "condition": "where filter==yomomma",
        "format_in": "",
        "format_out": ""
}

url = "http://localhost:8000/api/metadata/"
print(f"creating new metadata from {url}")
response = requests.post(url=url,json=data) #POST for creation
print(response.status_code)
print(response.text)