# LESSON 6: Libraries and Import
# ================================

# --- Importing libraries ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- NUMPY ---
# NumPy is used for mathematical operations on numbers

# Creating a numpy array (like a list but for math)
prices = np.array([500000, 750000, 300000, 900000, 450000])
print("Prices array:", prices)

# Useful math operations
print("Average price:", np.mean(prices))
print("Highest price:", np.max(prices))
print("Lowest price:", np.min(prices))
print("Standard deviation:", np.std(prices))

# --- PANDAS ---
# Pandas is used for working with tables of data (like Excel)

# Creating a simple table (called a DataFrame)
data = {
    "bedrooms": [3, 2, 4, 3, 2],
    "area":     [1500, 900, 2000, 1800, 1100],
    "price":    [500000, 750000, 300000, 900000, 450000]
}

df = pd.DataFrame(data)
print("\nOur house dataset:")
print(df)

# Basic info about the dataset
print("\nShape (rows, columns):", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nBasic statistics:")
print(df.describe())