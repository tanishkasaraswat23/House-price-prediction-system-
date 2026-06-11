import streamlit as st
import numpy as np
import pickle

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def predict_price(medinc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude):
    features = np.array([[medinc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    return prediction[0] * 100000

st.title("🏠 House Price Prediction System")
st.write("Enter the details below to predict the house price.")

st.sidebar.header("Enter House Details")

medinc = st.sidebar.slider("Median Income (in $10,000)", 0.5, 15.0, 5.0)
house_age = st.sidebar.slider("House Age (years)", 1, 52, 20)
ave_rooms = st.sidebar.slider("Average Rooms", 1.0, 15.0, 5.0)
ave_bedrms = st.sidebar.slider("Average Bedrooms", 1.0, 5.0, 1.0)
population = st.sidebar.slider("Population", 100, 10000, 1500)
ave_occup = st.sidebar.slider("Average Occupants", 1.0, 10.0, 3.0)
latitude = st.sidebar.slider("Latitude", 32.0, 42.0, 37.0)
longitude = st.sidebar.slider("Longitude", -125.0, -114.0, -120.0)

st.subheader("Selected House Details")
col1, col2 = st.columns(2)

with col1:
    st.write(f"Median Income: **${medinc * 10000:,.0f}**")
    st.write(f"House Age: **{house_age} years**")
    st.write(f"Average Rooms: **{ave_rooms}**")
    st.write(f"Average Bedrooms: **{ave_bedrms}**")

with col2:
    st.write(f"Population: **{population:,}**")
    st.write(f"Average Occupants: **{ave_occup}**")
    st.write(f"Latitude: **{latitude}**")
    st.write(f"Longitude: **{longitude}**")

if st.button("Predict Price"):
    price = predict_price(medinc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude)
    st.success(f"Estimated House Price: ${price:,.0f}")
    st.balloons()
st.write("---")
