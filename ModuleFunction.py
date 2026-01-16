# ModuleFunction.py
# Date: 2024-06-15
# Description: A Python program that demonstrates the use of modules and functions.

# Importing the math module and using its functions
import math
print("List of attributes and methods in math module:")
print(dir(math))  # Lists all attributes and methods in the math module


from math import sqrt
print("Using sqrt function from math module:")
print("Square root of 16 is:", sqrt(16))  # Using the sqrt function from math module