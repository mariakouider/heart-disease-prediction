from flask import Flask, render_template, request
import pickle
import pandas as pd
import os
import joblib


# Load the pre-trained Random Forest model I made in assignment 1
model_path = "model/rf_model.pkl"
rf_model = joblib.load(model_path)


# Create Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Expected form fields and their types so the end user can put them 
        form_fields = {
            'age': int,
            'sex': int,
            'cp': int,
            'trestbps': int,
            'chol': int,
            'fbs': int,
            'restecg': int,
            'thalach': int,
            'exang': int,
            'oldpeak': float,
            'slope': int,
            'ca': int,
            'thal': int
        }

        # Validate and parse input data into a dictionary
        input_data = {}
        for field, field_type in form_fields.items():
            value = request.form.get(field)
            if not value or value.strip() == '':
                raise ValueError(f"The field '{field}' is missing or empty.")
            input_data[field] = field_type(value)

        input_df = pd.DataFrame([input_data])

        # Make prediction from the pickle model 
        prediction = rf_model.predict(input_df)[0]
        probability = rf_model.predict_proba(input_df)[0][1]

        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"
        return render_template('result.html', result=result, probability=round(probability * 100, 2))

    except ValueError as ve:
        # Handle missing or invalid input data
        return render_template('result.html', error=f"Input Error: {ve}")
    except Exception as e:
        # Handle other unexpected errors
        return render_template('result.html', error=f"Unexpected Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


