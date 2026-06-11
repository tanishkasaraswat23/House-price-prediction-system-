import numpy as np
import pickle

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def predict_house_price(medinc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude):
    features = np.array([[medinc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    price = prediction[0] * 100000
    return price

print("=" * 45)
print("       HOUSE PRICE PREDICTION SYSTEM")
print("=" * 45)

house1 = predict_house_price(
    medinc=8.3252,
    house_age=41.0,
    ave_rooms=6.98,
    ave_bedrms=1.02,
    population=322.0,
    ave_occup=2.55,
    latitude=37.88,
    longitude=-122.23
)
print(f"House 1 Predicted Price: ${house1:,.0f}")

house2 = predict_house_price(
    medinc=3.5,
    house_age=20.0,
    ave_rooms=4.5,
    ave_bedrms=1.0,
    population=1500.0,
    ave_occup=3.0,
    latitude=34.0,
    longitude=-118.0
)
print(f"House 2 Predicted Price: ${house2:,.0f}")

house3 = predict_house_price(
    medinc=1.5,
    house_age=50.0,
    ave_rooms=3.0,
    ave_bedrms=1.0,
    population=5000.0,
    ave_occup=4.0,
    latitude=32.0,
    longitude=-117.0
)
print(f"House 3 Predicted Price: ${house3:,.0f}")

print("=" * 45)
print("Prediction system working!")