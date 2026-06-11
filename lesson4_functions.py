# LESSON 4: Functions
# ====================

# --- Basic function with no input ---
def greet():
    print("Welcome to House Price Predictor!")

# Calling the function
greet()

# --- Function with inputs (parameters) ---
def describe_house(bedrooms, area):
    print("This house has", bedrooms, "bedrooms")
    print("Total area is", area, "square feet")

# Calling with different inputs
describe_house(3, 1500)
describe_house(2, 900)

# --- Function that returns a value ---
def estimate_price(area, price_per_sqft):
    total = area * price_per_sqft
    return total

# Storing the returned value in a variable
price = estimate_price(1500, 200)
print("Estimated price:", price)

# --- Function with a default value ---
def estimate_price_v2(area, price_per_sqft=200):
    # price_per_sqft defaults to 200 if not provided
    total = area * price_per_sqft
    return total

print("Price with default rate:", estimate_price_v2(1500))
print("Price with custom rate:", estimate_price_v2(1500, 350))

# --- Realistic function for our project ---
def predict_house_price(bedrooms, area, bathrooms, age):
    # Simple formula for now (our ML model will replace this later)
    base_price = area * 200
    bedroom_bonus = bedrooms * 15000
    bathroom_bonus = bathrooms * 10000
    age_penalty = age * 2000
    
    final_price = base_price + bedroom_bonus + bathroom_bonus - age_penalty
    return final_price

# Testing our prediction function
predicted = predict_house_price(3, 1500, 2, 10)
print("Predicted house price:", predicted)