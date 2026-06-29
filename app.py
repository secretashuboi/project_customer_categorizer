import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Customer Categorizer", page_icon="📊")

st.title("📊 Customer Categorizer")
st.write("Enter the customer details below and click **Predict**.")

# -----------------------------
# Input Fields
# -----------------------------

age = st.number_input("Age", min_value=0)

education = st.number_input("Education (Encoded Value)", min_value=0)

marital_status = st.number_input("Marital Status (Encoded Value)", min_value=0)

parental_status = st.number_input("Parental Status (Encoded Value)", min_value=0)

children = st.number_input("Children", min_value=0)

income = st.number_input("Income", min_value=0.0)

total_spending = st.number_input("Total Spending", min_value=0.0)

days_as_customer = st.number_input("Days as Customer", min_value=0)

recency = st.number_input("Recency", min_value=0)

wines = st.number_input("Wines", min_value=0)

fruits = st.number_input("Fruits", min_value=0)

meat = st.number_input("Meat", min_value=0)

fish = st.number_input("Fish", min_value=0)

sweets = st.number_input("Sweets", min_value=0)

gold = st.number_input("Gold", min_value=0)

web = st.number_input("Web Purchases", min_value=0)

catalog = st.number_input("Catalog Purchases", min_value=0)

store = st.number_input("Store Purchases", min_value=0)

discount = st.number_input("Discount Purchases", min_value=0)

promo = st.number_input("Total Promo", min_value=0)

web_visits = st.number_input("Num Web Visits Month", min_value=0)

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Customer Category"):

    input_data = np.array([[

        age,

        education,

        marital_status,

        parental_status,

        children,

        income,

        total_spending,

        days_as_customer,

        recency,

        wines,

        fruits,

        meat,

        fish,

        sweets,

        gold,

        web,

        catalog,

        store,

        discount,

        promo,

        web_visits

    ]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Customer Category: {prediction[0]}")