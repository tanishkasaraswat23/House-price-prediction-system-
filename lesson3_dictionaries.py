# LESSON 3: Dictionaries
# =======================

# --- Creating a dictionary ---
house = {
    "bedrooms": 3,
    "area": 1500.5,
    "neighborhood": "Green Park",
    "has_garage": True,
    "price": 500000
}

# --- Accessing values by key ---
print("Bedrooms:", house["bedrooms"])
print("Area:", house["area"])
print("Price:", house["price"])

# --- Adding a new key-value pair ---
house["bathrooms"] = 2
print("After adding bathrooms:", house)

# --- Updating an existing value ---
house["price"] = 550000
print("Updated price:", house["price"])

# --- Getting all keys ---
print("All keys:", house.keys())

# --- Getting all values ---
print("All values:", house.values())

# --- Checking if a key exists ---
if "bedrooms" in house:
    print("Bedrooms key exists!")

# --- Looping through a dictionary ---
print("\nAll house details:")
for key, value in house.items():
    print(key, "→", value)