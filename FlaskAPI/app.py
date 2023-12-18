import flask
from flask import Flask, jsonify, request
import json
import pickle
import numpy as np

data_in = [1.0, 1.0, 540.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
        return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():
    request_json = request.get_json()
    x = request_json['input']
    
    x_in = np.array(x).reshape(1,-1)
    print(x_in)
    model = load_models()
    prediction = model.predict(x_in)[0]
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
    application.run(debug=True)

