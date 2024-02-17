import joblib
from flask import Flask, jsonify, render_template, request
import numpy as np

app = Flask(__name__)

# Load the model
classmodel = None  # Load model dynamically

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# API endpoint for prediction
@app.route('/predict_api', methods=['POST'])
def predict_api():
    global classmodel
    if classmodel is None:
        classmodel = joblib.load('bank_churn.joblib')
    data = request.json['data']
    input_data = np.array(list(data.values())).reshape(1, -1)
    output = classmodel.predict(input_data)
    output_value = int(output)
    return jsonify(output_value)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    global classmodel
    if classmodel is None:
        classmodel = joblib.load('bank_churn.joblib')
    data = [float(x) for x in request.form.values()]
    final_input = np.array(data).reshape(1, -1)
    output = classmodel.predict(final_input)[0]
    
    # Modify prediction text based on output value
    prediction_text = "Bank churn likely" if output == 1 else "Bank churn unlikely"
    
    return render_template("home.html", prediction_text=prediction_text)

