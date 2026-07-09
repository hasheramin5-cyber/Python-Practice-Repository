# A Program to insert an element at a specific position in a list.

colors = ["Red", "Green", "Blue"]

print("\nList:", colors)

index = int(input("Enter the index: "))
color = input("Enter a color: ").title()

colors.insert(index, color)

print("Updated List is:", colors)

# Explanation:
# The program inserts a new element at a specific index using the insert() method. Existing elements from that position onward are shifted one place to the right.