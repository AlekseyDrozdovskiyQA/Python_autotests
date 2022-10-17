import requests

#Создание нового питомца
response_new_pet = requests.post("https://petstore.swagger.io/v2/pet", json = {
  "id": 250,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Neverr",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}) 
print(response_new_pet.text)

#Сменить имя питомца
response_change_name = requests.put("https://petstore.swagger.io/v2/pet", json = {
  "id": 250,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "NeverLatee",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"  
}) 
print(response_change_name.text)

#Поиск питомца по id
response_find_pet = requests.get("https://petstore.swagger.io/v2/pet/250")
print(response_find_pet.text)