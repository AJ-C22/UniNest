from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

class model_input(BaseModel):

    Bedrooms : int
    Bathrooms : float
    Size : int
    Guelph : int
    Hamilton : int 
    Kitchener : int 
    London : int
    Ottawa : int
    Toronto : int 
    Apartment : int 
    Basement : int 
    Condo : int
    Duplex : int 
    House : int
    Townhouse : int

#load saved model
housing_model = pickle.load(open('housing_model.sav', 'rb')) 

@app.post('/housing_prediction')
def housing_pred(input_parameters : model_input):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    bed = input_dictionary['Bedrooms']
    bath = input_dictionary['Bathrooms']
    size = input_dictionary['Size']
    guelph = input_dictionary['Guelph']
    hamilton = input_dictionary['Hamilton']
    kitchener = input_dictionary['Kitchener']
    london = input_dictionary['London']
    ottawa = input_dictionary['Ottawa']
    toronto = input_dictionary['Toronto']
    apartment = input_dictionary['Apartment']
    basement = input_dictionary['Basement']
    condo = input_dictionary['Condo']
    duplex = input_dictionary['Duplex']
    house = input_dictionary['House']
    townhouse = input_dictionary['Townhouse']


    input_list = [bed, bath, size, guelph, hamilton, kitchener, london, ottawa, toronto, apartment, basement, condo, duplex, house, townhouse]

    prediction = housing_model.predict([input_list])

