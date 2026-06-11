# STEP 4: Data Preprocessing
# ===========================
# Yahan hum data ko ML model ke liye ready karenge

import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler

# ================================================
# PART 1: Load data (same as step 3)
# ================================================
california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df["MedHouseVal"] = california.target

print("Dataset loaded successfully!")
print("Shape:", df.shape)

# ================================================
# PART 2: Separate Features and Target
# ================================================

# X = features (inputs) → everything except price
# y = target (output)   → only the price column

X = df.drop("MedHouseVal", axis=1)  # remove target column
y = df["MedHouseVal"]               # keep only target column

print("\nFeatures shape (X):", X.shape)
print("Target shape (y):", y.shape)

print("\nFirst 3 rows of X (features):")
print(X.head(3))

print("\nFirst 3 values of y (target/prices):")
print(y.head(3))

# ================================================
# PART 3: Feature Scaling
# ================================================

# StandardScaler makes all features have:
# mean = 0 and standard deviation = 1
# This brings all columns to same scale

scaler = StandardScaler()

# fit_transform does two things:
# 1. fit    → learns the mean and std of each column
# 2. transform → scales the data using that information
X_scaled = scaler.fit_transform(X)

# Convert back to DataFrame so it looks nice
X_scaled_df = pd.DataFrame(X_scaled, columns=california.feature_names)

print("\nBefore scaling (first row):")
print(X.iloc[0])

print("\nAfter scaling (first row):")
print(X_scaled_df.iloc[0])

print("\nData preprocessing complete!")
print("X_scaled shape:", X_scaled_df.shape)