import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pickle
import os

california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df["MedHouseVal"] = california.target

X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
r2 = r2_score(y_test, y_pred)
print(f"Model R2 Score: {r2:.4f}")

os.makedirs("models", exist_ok=True)

with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model saved: models/model.pkl")
print("Scaler saved: models/scaler.pkl")

with open("models/model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    loaded_scaler = pickle.load(f)

print("\nModel loaded successfully!")

sample = np.array([[8.3252, 41.0, 6.984, 1.023, 322.0, 2.555, 37.88, -122.23]])
sample_scaled = loaded_scaler.transform(sample)
prediction = loaded_model.predict(sample_scaled)
print(f"Test prediction: ${prediction[0] * 100000:,.0f}")