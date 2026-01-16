# Condition.py
# Date: 2024-06-15
# Description: A Python program that demonstrates conditional statements.

# Taking input for age
age = input("Enter your age: ")

# Conditional statements to check age category
if(int(age) >= 18):
    print("You're an adult.")
    print("You can vote.")
elif(int(age) > 0 and int(age) < 18):
    print("You're a minor.")
    print("You cannot vote.")
else:
    print("Invalid age entered.")

# Final message
print("Thank you for using the age checker.")