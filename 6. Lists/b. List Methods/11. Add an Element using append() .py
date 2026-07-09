# A Program to add an element to the end of a list using the append() method.

fruits = ["Apple", "Banana", "Mango"]

print("\nBefore Updating List is:", fruits)
fruit = input("Enter a fruit to add: ").title()

fruits.append(fruit)

print("\nAfter Updating List is:", fruits)

# Explanation:
# The program adds a new element to the end of the list using the append() method. This method inserts only one element at a time and modifies the original list.