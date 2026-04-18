import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.title("💳 UPI Fraud Detection")

model = joblib.load("models/upi_fraud_model.pkl")
features = joblib.load("models/features.pkl")

# -------- USER INPUT -------- #

amount = st.number_input("Amount (INR)", value=1000)

transaction_type = st.selectbox(
    "Transaction Type",
    ["TRANSFER", "PAYMENT", "CASH_OUT"]
)

merchant_category = st.selectbox(
    "Merchant Category",
    ["shopping", "food", "travel"]
)

sender_state = st.selectbox(
    "Sender State",
    ["MH", "DL", "KA"]
)

receiver_bank = st.selectbox(
    "Receiver Bank",
    ["SBI", "HDFC", "ICICI"]
)

device_type = st.selectbox(
    "Device Type",
    ["mobile", "desktop"]
)

hour_of_day = st.slider("Hour of Day", 0, 23, 12)

is_weekend = st.selectbox("Is Weekend", [0, 1])

# -------- CONVERT TO MODEL FORMAT -------- #

input_dict = {
    "amount (INR)": amount,
    "transaction type": transaction_type,
    "merchant_category": merchant_category,
    "sender_state": sender_state,
    "receiver_bank": receiver_bank,
    "device_type": device_type,
    "hour_of_day": hour_of_day,
    "is_weekend": is_weekend
}

# Convert input to DataFrame
input_df = pd.DataFrame([input_dict])

# 🔥 IMPORTANT FIX: force categorical columns to string
categorical_cols = [
    "transaction type",
    "merchant_category",
    "sender_state",
    "receiver_bank",
    "device_type"
]

for col in categorical_cols:
    input_df[col] = input_df[col].astype(str)

# Convert input to DataFrame
input_df = pd.DataFrame([input_dict])

# Convert categorical columns to string
categorical_cols = [
    "transaction type",
    "merchant_category",
    "sender_state",
    "receiver_bank",
    "device_type"
]

for col in categorical_cols:
    input_df[col] = input_df[col].astype(str)

# One-hot encoding
input_df = pd.get_dummies(input_df)

# ✅ FINAL FIX: match training features EXACTLY
input_df = input_df.reindex(columns=features, fill_value=0)
# -------- FIX ENDS HERE -------- #

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("🚨 Fraud Transaction")
    else:
        st.success("✅ Legitimate Transaction")