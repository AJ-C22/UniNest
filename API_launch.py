import json
import requests

url = "http://127.0.0.1:8000/housing_prediction"

input_data_for_model = {

    'Bedrooms' : 2,
    'Bathrooms' : 1,
    'Size' : 800,
    'Guelph' : 1,
    'Hamilton' : 0,
    'Kitchener' : 0,
    'London' : 0,
    'Ottawa' : 0,
    'Toronto' : 0,
    'Apartment' : 0,
    'Basement' : 1,
    'Condo' : 0,
    'Duplex' : 0,
    'House' : 0,
    'Townhouse' : 0

}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print("hello")