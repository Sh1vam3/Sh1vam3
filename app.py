from flask import Flask, request, jsonify
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)

CORS(app) 

# Load the model
with open('heart_disease_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Extract and prepare features
    age = data.get('age')
    cp = data.get('cp')
    thalach = data.get('thalach')

    if age is None or cp is None or thalach is None:
        return jsonify({'error': 'Invalid input'}), 400

    # Create DataFrame for prediction
    user_data = pd.DataFrame([[age, cp, thalach]], columns=['age', 'cp', 'thalach'])
    prediction = model.predict(user_data)[0]
    result = "Heart Disease" if prediction == 1 else "No Heart Disease"
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
