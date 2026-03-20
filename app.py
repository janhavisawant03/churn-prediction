import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("churn_model.pkl", "rb"))

st.title("Bank Customer Churn Prediction")

credit = st.number_input("Credit Score")
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age")
tenure = st.number_input("Tenure")
balance = st.number_input("Balance")
products = st.number_input("Number of Products")
card = st.selectbox("Has Credit Card", [0, 1])
active = st.selectbox("Is Active Member", [0, 1])
salary = st.number_input("Estimated Salary")
geo = st.selectbox("Geography", ["Germany", "Spain"])

gender = 1 if gender == "Male" else 0


geo_ge = 1 if geo == "Germany" else 0
geo_sp = 1 if geo == "Spain" else 0

if st.button("Predict"):
    data = np.array([[credit, geo_ge, geo_sp, gender, age, tenure,
                  balance, products, card, active, salary]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer will Stay")