# A Program to create a copy of a list.

fruits = ["Apple", "Banana", "Mango"]

copied_list = fruits.copy()

print("\nOriginal List:", fruits)
print("Copied List:  ", copied_list)

# Explanation:
# The program creates a copy of a list using the copy() method. Both lists contain the same elements, but they are stored as separate list objects. Changes made to one list do not affect the other.