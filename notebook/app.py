import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("../models/diabetes_model.pkl")

st.title("🩺 Diabetes Prediction")

st.write("Enter the patient details below:")

pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose", min_value=0)
blood_pressure = st.number_input("Blood Pressure", min_value=0)
skin_thickness = st.number_input("Skin Thickness", min_value=0)
insulin = st.number_input("Insulin", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
age = st.number_input("Age", min_value=1)

if st.button("Predict"):
    data = np.array([[pregnancies, glucose, blood_pressure,
                      skin_thickness, insulin,
                      bmi, dpf, age]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("The person is Diabetic")
    else:
        st.success("The person is Non-Diabetic")
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("The person is Diabetic")
    else:
        st.success("The person is Non-Diabetic")