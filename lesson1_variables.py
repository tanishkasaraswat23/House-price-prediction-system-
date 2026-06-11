# LESSON 1: Variables and Data Types
# ===================================

# --- Integer (whole number) ---
number_of_bedrooms = 3
print("Bedrooms:", number_of_bedrooms)

# --- Float (decimal number) ---
house_area = 2000.0
print("Area in sq ft:", house_area)

# --- String (text) ---
neighborhood = "Green Park"
print("Neighborhood:", neighborhood)

# --- Boolean (True or False) ---
has_garage = True
print("Has Garage:", has_garage)

# --- Checking the TYPE of a variable ---
print(type(number_of_bedrooms))   # will show: <class 'int'>
print(type(house_area))           # will show: <class 'float'>
print(type(neighborhood))         # will show: <class 'str'>
print(type(has_garage))           # will show: <class 'bool'>

# --- Simple Math with variables ---
price_per_sqft = 200.0
total_price = house_area * price_per_sqft
print("Estimated Price:", total_price)