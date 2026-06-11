import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pickle

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

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

y_pred = model.predict(X_test_scaled)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("=" * 40)
print("       MODEL EVALUATION RESULTS")
print("=" * 40)
print(f"MAE   : {mae:.4f} (${mae*100000:,.0f})")
print(f"MSE   : {mse:.4f}")
print(f"RMSE  : {rmse:.4f} (${rmse*100000:,.0f})")
print(f"R2    : {r2:.4f}")
print("=" * 40)

if r2 >= 0.9:
    print("Excellent model!")
elif r2 >= 0.7:
    print("Good model!")
elif r2 >= 0.5:
    print("Average model!")
else:
    print("Model needs improvement!")

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.3, color="steelblue")
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         color="red", linewidth=2)
plt.title("Actual Prices vs Predicted Prices")
plt.xlabel("Actual Price (in $100,000)")
plt.ylabel("Predicted Price (in $100,000)")
plt.savefig("data/actual_vs_predicted.png")
plt.show()
print("\nGraph saved: data/actual_vs_predicted.png")