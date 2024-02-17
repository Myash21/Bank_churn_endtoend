import pickle
from flask import Flask, jsonify, render_template, url_for, app, request
import pandas as pd
import numpy as np

#Load the model
app = Flask(__name__)
classmodel = pickle.load(open('bank_churn.pkl','rb'))

#home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    input_data = np.array(list(data.values())).reshape(1,-1)
    output = classmodel.predict(input_data)
    output_value = int(output)
    return jsonify(output_value)

if __name__=="__main__":
    app.run(debug=True)
