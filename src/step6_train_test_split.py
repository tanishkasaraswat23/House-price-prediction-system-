# STEP 6: Train-Test Split
# =========================
# Yahan hum data ko training aur testing mein divide karenge

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# ================================================
# PART 1: Load and prepare data
# ================================================
california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df["MedHouseVal"] = california.target

# Separate features and target
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

print("Full dataset shape:")
print("X (features):", X.shape)
print("y (target):", y.shape)

# ================================================
# PART 2: Train-Test Split
# ================================================

# test_size=0.2  → 20% data testing ke liye
# random_state=42 → ensures same split every time
#                   (42 is just a convention, any number works)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("\nAfter Train-Test Split:")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

# ================================================
# PART 3: Feature Scaling
# ================================================

# IMPORTANT RULE:
# Scaler ko sirf training data pe fit karo
# Testing data pe sirf transform karo
# Kyun? Kyunki test data "unseen" rehna chahiye

scaler = StandardScaler()

# fit_transform on training data
X_train_scaled = scaler.fit_transform(X_train)

# Only transform on testing data (no fit!)
X_test_scaled = scaler.transform(X_test)

print("\nAfter Scaling:")
print("X_train_scaled shape:", X_train_scaled.shape)
print("X_test_scaled shape:", X_test_scaled.shape)

print("\nTrain-Test Split complete!")
print("Model training ke liye data ready hai!")