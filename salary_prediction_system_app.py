
import streamlit as st
import pandas as pd
import joblib

# Load saved objects
model = joblib.load("salary_model.pkl")
scaler = joblib.load("salary_scaler.pkl")
columns = joblib.load("salary_columns.pkl")

st.title("Employee Salary Prediction")

age = st.number_input("Age",18,65)
experience = st.number_input("Years of Experience",0,40)
performance = st.slider("Performance Score",1.0,5.0)

city = st.selectbox("City",
["Bangalore","Hyderabad","Pune","Delhi","Mumbai","Chennai"])

department = st.selectbox("Department",
["Engineering","Marketing","Sales","HR","Finance","Operations"])

input_data = pd.DataFrame({
"age":[age],
"years_experience":[experience],
"performance_score":[performance],
"city":[city],
"department":[department]
})

# One-hot encoding
input_data = pd.get_dummies(input_data)

# Match training columns
input_data = input_data.reindex(columns=columns, fill_value=0)

# Prediction
if st.button("Predict Salary"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Salary: ${prediction[0]:,.2f}")
