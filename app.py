#from flask import Flask, request, jsonify  # Not needed in Streamlit but okay if reused elsewhere
import streamlit as st
import joblib
import numpy as np

# Load your trained model
model = joblib.load("model.pkl")

st.title("📞 Customer Churn Prediction (Telecom)")
st.write("Provide customer details to predict churn:")

# User inputs (only required features)
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Has Partner", ["Yes", "No"])
dependents = st.selectbox("Has Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (in months)", min_value=0)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

# Encoding inputs (based on model training)
inputs = [
    0,  # gender (default to Female)
    senior,
    1 if partner == "Yes" else 0,
    1 if dependents == "Yes" else 0,
    tenure,
    1 if phone_service == "Yes" else 0,
    0,  # multiple_lines (default to No)
    1 if internet_service == "DSL" else 0,
    1 if internet_service == "Fiber optic" else 0,
    0,  # online_security (default to No)
    0,  # online_backup (default to No)
    0,  # device_protection (default to No)
    0,  # tech_support (default to No)
    0,  # streaming_tv (default to No)
    0,  # streaming_movies (default to No)
    0 if contract == "Month-to-month" else 1 if contract == "One year" else 2,
    0,  # paperless_billing (default to No)
    ["Electronic check", "Mailed check", "Bank transfer", "Credit card"].index(payment),
    monthly,
    total
]

# Predict button
if st.button("Predict Churn"):
    input_array = np.array(inputs).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    
    if prediction == 1:
        st.error("⚠️ This customer is likely to churn.")
    else:
        st.success("✅ This customer is likely to stay.")
    
