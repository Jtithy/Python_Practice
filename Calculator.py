# Calculator.py
# Date: 2024-06-15
# Description: A Python program that imports and runs various mathematical and string operations.

# Simple calculator functionality
first = input("Enter first number: ")
operator = input("Enter operator (+, -, *, /, %, **): ")
second = input("Enter second number: ")

# Performing calculation based on the operator
if operator == "+":
    print("Result: ", int(first)+int(second))
elif operator == "-":
    print("Result: ", int(first)-int(second))
elif operator == "*":
    print("Result: ", int(first)*int(second))
elif operator == "/":
    print("Result: ", int(first)/int(second))
elif operator == "%":
    print("Result: ", int(first)%int(second))
elif operator == "**":
    print("Result: ", int(first)**int(second))
else:
    print("Invalid operator")

# Final message
print("Thank you for using the calculator program!")