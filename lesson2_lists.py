# LESSON 2: Lists
# ================

# --- Creating a list ---
house_prices = [500000, 750000, 300000, 900000, 450000]
print("All prices:", house_prices)

# --- Accessing items by index ---
# Remember: index starts at 0, not 1
print("First house price:", house_prices[0])   # 500000
print("Second house price:", house_prices[1])  # 750000
print("Last house price:", house_prices[-1])   # -1 always means last item

# --- How many items in the list? ---
print("Number of houses:", len(house_prices))

# --- Adding a new price to the list ---
house_prices.append(620000)
print("After adding new house:", house_prices)

# --- Lists can store different data types too ---
house_features = [3, 1500.5, "Green Park", True]
print("House features:", house_features)
# bedrooms=3, area=1500.5, neighborhood="Green Park", has_garage=True

# --- Slicing: getting a portion of a list ---
first_three = house_prices[0:3]
print("First three prices:", first_three)