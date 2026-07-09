# Import libraries# Import libraries
import streamlit as st
import joblib

# Load model and scaler

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Title
st.title("🏠 House Price Prediction App")

# Description
st.write("Enter house details and predict the house price using Random Forest.")

medinc = st.number_input("Median Income")
houseage = st.number_input("House Age")
averooms = st.number_input("Average Rooms")
avebedrms = st.number_input("Average Bedrooms")
population = st.number_input("Population")
aveoccup = st.number_input("Average Occupancy")
latitude = st.number_input("Latitude")
longitude = st.number_input("Longitude")


# Predict button

if st.button("Predict Price"):

    # Create input data
    input_data = [[
        medinc,
        houseage,
        averooms,
        avebedrms,
        population,
        aveoccup,
        latitude,
        longitude
    ]]

    # Scale input
    input_data_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_data_scaled)

    # Display result
    st.success(f"🏠 Predicted House Price: ${prediction[0]*100000:,.2f}")


    st.markdown("---")
st.write("Built with Python, Scikit-Learn, Random Forest and Streamlit")