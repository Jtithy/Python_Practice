# MarksList.py
# Date: 2024-06-15
# Description: A Python program that creates a list of marks and prints them.


marks = [85, 90, 78, 92, 88]
print("Marks List:", marks)

# Modifying the list
print("Appending a new mark (95) of Economics to the list:")
marks.append(95)
print("Updated Marks List:", marks)

# Inserting a new mark at a specific index
print("Inserting a new mark (92) of Computer Science at index 2:")
marks.insert(2, 92) # Inserting at index 2
print("Updated Marks List:", marks)    

# Checking for presence of a specific mark
print("Checking specific mark (90) in the list:")
if 90 in marks:
    print("90 is present in the list.")
else:
    print("90 is not present in the list.")

# Checking length of the marks list
print("Checking length of the marks list:")
print(len(marks))
print("Marks List:", marks)

# Removing a specific mark
print("Removing the mark (78) from the list:")
marks.remove(78)
print("Updated Marks List:", marks)

# Clearing the entire marks list
print("Clearing the entire marks list:")
marks.clear()
print("Cleared Marks List:", marks)