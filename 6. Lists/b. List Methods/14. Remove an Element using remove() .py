# A Program to remove an element from a list using the remove() method.

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("\nList:", fruits)
fruit = input("Enter the fruit to remove: ").title()

if fruit in fruits:
    fruits.remove(fruit)
    print("Updated List: ", fruits)
else:
    print("Fruit not found.")

# Explanation:
# The program removes the first occurrence of a specified element using the remove() method. Before removing the element, it checks whether the element exists in the list to avoid an error.