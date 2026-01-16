# Input.py
# Date: 2024-06-15
# Description: A Python program that demonstrates input handling.

first = input("Enter 1st number: ")
second = input("Enter 2nd number: ")

sum = int(first) + int(second)

# three ways to print integer sum
print(sum)
print("The sum is: " + str(sum))
print("The sum is: " + sum.__str__())