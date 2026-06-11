# STEP 5: Data Visualization
# ===========================
# Yahan hum data ko graphs ke zariye samjhenge

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# ================================================
# PART 1: Load data
# ================================================
california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df["MedHouseVal"] = california.target

# ================================================
# PART 2: Distribution of House Prices
# ================================================

plt.figure(figsize=(10, 6))
plt.hist(df["MedHouseVal"], bins=50, color="steelblue", edgecolor="black")
plt.title("Distribution of House Prices")
plt.xlabel("House Price (in $100,000)")
plt.ylabel("Number of Houses")
plt.savefig("data/price_distribution.png")
plt.show()
print("Graph 1 saved!")

# ================================================
# PART 3: Correlation Heatmap
# ================================================

# Correlation tells us:
# Which features affect house price the most?
# Value close to 1  = strong positive relationship
# Value close to -1 = strong negative relationship
# Value close to 0  = no relationship

correlation = df.corr()
print("\nCorrelation with House Price:")
print(correlation["MedHouseVal"].sort_values(ascending=False))

# ================================================
# PART 4: Most Important Feature vs Price
# ================================================

# MedInc (income) has highest correlation with price
plt.figure(figsize=(10, 6))
plt.scatter(df["MedInc"], df["MedHouseVal"],
            alpha=0.3, color="steelblue")
plt.title("Income vs House Price")
plt.xlabel("Median Income")
plt.ylabel("House Price (in $100,000)")
plt.savefig("data/income_vs_price.png")
plt.show()
print("Graph 2 saved!")

# ================================================
# PART 5: House Age vs Price
# ================================================

plt.figure(figsize=(10, 6))
plt.scatter(df["HouseAge"], df["MedHouseVal"],
            alpha=0.3, color="coral")
plt.title("House Age vs House Price")
plt.xlabel("House Age (years)")
plt.ylabel("House Price (in $100,000)")
plt.savefig("data/age_vs_price.png")
plt.show()
print("Graph 3 saved!")

print("\nAll visualizations complete!")