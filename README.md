# 💳 UPI Fraud Detection

This project is a simple attempt to understand how machine learning can be used to detect fraudulent UPI transactions.

With the rapid growth of digital payments, fraud detection has become an important problem. In this project, I built a machine learning model and connected it with a small web interface so that anyone can input transaction details and check whether it looks suspicious or not.

---

## What this project does

The application takes a few transaction details like amount, type of transaction, device used, etc., and predicts whether the transaction is:

* ✅ Legitimate
* 🚨 Fraudulent

The goal is not to build a production-level system, but to demonstrate how data preprocessing, model training, and deployment come together in a complete pipeline.

---

## How it works (in simple terms)

1. The dataset is cleaned and preprocessed
2. Categorical values are converted into numerical format
3. A machine learning model is trained on the data
4. The model is saved using `joblib`
5. A Streamlit app is created to take user input
6. Input is converted into the same format as training data
7. Model predicts the result and shows it on screen

---

## Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* Streamlit
* Joblib

---

## Project Structure

UPI_FRAUD_DETECTION/
│
├── models/
│   ├── upi_fraud_model.pkl
│   ├── features.pkl
│
├── app.py
├── predict.py
├── requirements.txt
└── README.md

---

##  How to run this project

Clone the repository:

git clone https://github.com/YOUR_USERNAME/upi-fraud-detection.git
cd upi-fraud-detection

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

Then open:

http://localhost:8501

---

## About the model

* The model is trained using a classification algorithm (Random Forest)
* Since fraud datasets are usually imbalanced, handling that was important
* Feature encoding (one-hot encoding) is used to match training format

---

## Limitations

* The model is trained on a sample dataset, so predictions are not perfect
* In my current version, the model sometimes predicts "legitimate" more often due to imbalance
* Real-world systems require much more data and tuning

---

##  What I learned from this project

* How to preprocess real-world datasets
* Importance of feature consistency between training and prediction
* How to save and load models
* How to build a simple frontend using Streamlit
* Debugging model-related errors (feature mismatch, encoding issues, etc.)

---

##  Future improvements

* Improve model accuracy with better techniques
* Use advanced algorithms like XGBoost
* Add proper validation and metrics display
* Deploy the app online
* Improve UI design

---

## 👩‍💻 Author

Shivani

---

## ⭐ Final note

This project was built as part of my learning journey in machine learning and deployment.
It’s not perfect, but it helped me understand the full pipeline from data to a working application.

If you find it useful or interesting, feel free to explore or improve it 🙂
