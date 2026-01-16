# WhileLoop.py
# Date: 2024-06-15
# Description: A Python program that demonstrates a while loop.

# Printing a pattern using while loop
iteration = 1

# Upword triangle pattern
print("Upword triangle pattern:")

while iteration <= 5:
    print(iteration * "*")
    iteration += 1

# Downword triangle pattern
print("Downword triangle pattern:")

iteration = 5
while iteration >= 1:
    print(iteration * "*")
    iteration -= 1

