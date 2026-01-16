# List.py
# Date: 2024-06-15
# Description: A Python program that demonstrates list operations.

print("Creating a list of marks:")
marks = [96, 98, 90, 89, 99] # index 0 to 4
print("Marks List:", marks)

print("Printing marks subject wise in 0 to 4:")
print("Math:", marks[0])
print("Science:", marks[1])
print("English:", marks[2])
print("History:", marks[3])
print("Geography:", marks[4])

print("Printing marks subject wise in 4 to 0:")
print("Math:", marks[-5])
print("Science:", marks[-4])
print("English:", marks[-3])
print("History:", marks[-2])
print("Geography:", marks[-1])

print("Printing only Math and Science:")
print(marks[0:2]) # Slicing from index 0 to 1

# Using loop
print("Printing all marks using for loop:")
for score in marks:
    print(score)
