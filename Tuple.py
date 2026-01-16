# Tuple.py
# Date: 2024-06-15
# Description: A Python program that demonstrates tuple operations.


# Creating a tuple
marks = (90, 85, 70, 90, 88)

# marks[0] = 95 : This will raise a TypeError
#Tuple cannot be changed
print("Marks Tuple:", marks)

print("Count of 90 in the tuple:", marks.count(90))  # Count of 90 in the tuple
print("Index of 88 in the tuple:", marks.index(88))  # Index of 88 in the tuple