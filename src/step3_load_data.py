# STEP 3: Loading Data With Pandas
# ==================================
# This is the first step of our actual ML project.
# We load the California Housing Dataset and explore it.

# --- Import libraries ---
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing

# ================================================
# PART 1: Load the dataset
# ================================================

# fetch_california_housing() loads the dataset from sklearn
# It gives us features and target separately
california = fetch_california_housing()

# Convert to a pandas DataFrame so we can work with it easily
# california.data      → contains all the feature columns
# california.feature_names → contains the column names
df = pd.DataFrame(california.data, columns=california.feature_names)

# Add the target column (house prices) to our DataFrame
# california.target → contains the house prices
df["MedHouseVal"] = california.target

# ================================================
# PART 2: Explore the dataset
# ================================================

# How many rows and columns?
print("Shape of dataset (rows, columns):", df.shape)

# Show first 5 rows
print("\nFirst 5 rows of dataset:")
print(df.head())

# Show last 5 rows
print("\nLast 5 rows of dataset:")
print(df.tail())

# Show column names
print("\nColumn names:")
print(df.columns.tolist())

# ================================================
# PART 3: Understand the data
# ================================================

# Basic statistics for every column
print("\nBasic statistics:")
print(df.describe())

# Check data types of each column
print("\nData types:")
print(df.dtypes)

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# ================================================
# PART 4: Look at features and target separately
# ================================================

# Features (inputs to our model)
features = california.feature_names
print("\nFeature columns (inputs):")
print(features)

# Target (what we want to predict)
print("\nTarget column (output):")
print("MedHouseVal")

print("\nAverage house value:", df["MedHouseVal"].mean())
print("Highest house value:", df["MedHouseVal"].max())
print("Lowest house value:", df["MedHouseVal"].min())