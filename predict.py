import joblib
import numpy as np

# Load model
model = joblib.load("models/upi_fraud_model.pkl")

def predict_fraud(input_data):
    data = np.array([input_data])

    prediction = model.predict(data)
    probability = model.predict_proba(data)

    return prediction[0], probability[0][1]