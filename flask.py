from flask import Flask_request
from flask_restful import Resource, Api
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
#
CORS(app)
#creating an API object
api = Api(app)

#prediction api call
class prediction(Resource):
    def get(self, size, bedrooms, bathrooms, city, style):
        