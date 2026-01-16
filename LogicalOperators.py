# LogicalOperators.py
# Date: 2024-06-15
# Description: A Python program that demonstrates logical operators.

#Taking input for logical operations
num1 = input("Enter 1st number:")
num2 = input("Enter 2nd number:")

#Performing logical operations
print("Logical AND:" , (int(num1) > int(num2)) and (int(num2) < int(num1))) # Logical AND Operator
print("Logical OR:" , (int(num1) > int(num2)) or (int(num2) > int(num1))) # Logical OR Operator
print("Logical NOT:" , not(int(num1) == int(num2))) # Logical NOT Operator