import streamlit as st
import pandas as pd
import joblib

# Load saved objects
model = joblib.load("salary_model.pkl")
scaler = joblib.load("salary_scaler.pkl")
columns = joblib.load("salary_columns.pkl")

st.title("Employee Salary Prediction")

st.write("Enter employee details to predict salary")

# User inputs
age = st.number_input("Age", 18, 65, 25)
experience = st.number_input("Years of Experience", 0, 40, 5)
performance = st.slider("Performance Score", 1.0, 5.0, 3.0)

city = st.selectbox(
    "City",
    ["Bangalore","Hyderabad","Pune","Delhi","Mumbai","Chennai"]
)

department = st.selectbox(
    "Department",
    ["Engineering","Marketing","Sales","HR","Finance","Operations"]
)

# Create dataframe
input_data = pd.DataFrame({
    "age":[age],
    "years_experience":[experience],
    "performance_score":[performance],
    "city":[city],
    "department":[department]
})

# ---------- STEP 1: SCALE NUMERIC FEATURES ----------
numeric_cols = ["age","years_experience","performance_score"]
input_data[numeric_cols] = scaler.transform(input_data[numeric_cols])

# ---------- STEP 2: ONE HOT ENCODE ----------
input_data = pd.get_dummies(input_data)

# ---------- STEP 3: ALIGN WITH TRAINING COLUMNS ----------
input_data = input_data.reindex(columns=columns, fill_value=0)

# ---------- PREDICTION ----------
if st.button("Predict Salary"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Salary: ${prediction:,.2f}")
