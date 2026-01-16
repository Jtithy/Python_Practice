# Break&Continue.py
# Date: 2024-06-15
# Description: A Python program that demonstrates the use of break and continue statements in loops.

# List of students
students = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Task1 : Using break statement in a for loop
print("Using break statement:")
for student in students:
    if student == "David":
        break;  # Exit the loop when student is David
    print(student)

# Task2 : Using continue statement in a for loop
print("Using continue statement:")
for student in students:
    if student == "David":
        continue;  # Skip the iteration when student is David
    print(student)

