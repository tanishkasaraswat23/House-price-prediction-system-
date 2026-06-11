# LESSON 7: Reading Error Messages
# ==================================
# In this lesson we will INTENTIONALLY cause errors
# and then fix them one by one
# This is how you learn to debug code

# ================================================
# ERROR 1: NameError
# ================================================
# Uncomment the line below to see the error
# print(house_price)
# Fix: define the variable first
house_price = 500000
print("House price:", house_price)

# ================================================
# ERROR 2: SyntaxError
# ================================================
# Uncomment to see error
# print("Hello"
# Fix: closing bracket was missing
print("Hello from lesson 7")

# ================================================
# ERROR 3: IndentationError
# ================================================
# Uncomment to see error
# def greet():
# print("hello")    ← not indented
# Fix: indent code inside function
def greet():
    print("Greet function works!")
greet()

# ================================================
# ERROR 4: TypeError
# ================================================
# Uncomment to see error
# result = "The price is " + 500000
# Fix: convert number to string first
result = "The price is " + str(500000)
print(result)

# ================================================
# ERROR 5: ModuleNotFoundError
# ================================================
# Uncomment to see error
# import supermagiclib
# Fix: install it using pip install supermagiclib
# OR check if you spelled the library name correctly

# ================================================
# PRACTICE: Read this error without running it
# ================================================
# Traceback (most recent call last):
#   File "model.py", line 12, in <module>
#     prediction = predict(area, bedrooms)
# TypeError: predict() takes 1 positional argument but 2 were given
#
# What does this error mean?
# Answer: the predict function was defined to take only 1 input
# but we called it with 2 inputs

print("\nAll errors understood and fixed!")