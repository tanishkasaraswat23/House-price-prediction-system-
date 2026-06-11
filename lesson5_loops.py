# LESSON 5: Loops
# ================

# --- Basic for loop ---
house_prices = [500000, 750000, 300000, 900000, 450000]

print("All house prices:")
for price in house_prices:
    print(price)

# --- Loop with index using enumerate ---
print("\nPrices with house number:")
for index, price in enumerate(house_prices):
    print("House", index + 1, "costs", price)

# --- Loop through a range of numbers ---
print("\nCounting from 1 to 5:")
for number in range(1, 6):
    print(number)

# --- Loop through a dictionary ---
house = {
    "bedrooms": 3,
    "area": 1500,
    "bathrooms": 2,
    "price": 500000
}

print("\nHouse details:")
for key, value in house.items():
    print(key, ":", value)

# --- Loop with a condition inside ---
print("\nExpensive houses (above 600000):")
for price in house_prices:
    if price > 600000:
        print(price, "is expensive")
    else:
        print(price, "is affordable")

# --- Building a new list using a loop ---
discounted_prices = []
for price in house_prices:
    discounted = price * 0.9    # 10% discount
    discounted_prices.append(discounted)

print("\nOriginal prices:", house_prices)
print("Discounted prices:", discounted_prices)