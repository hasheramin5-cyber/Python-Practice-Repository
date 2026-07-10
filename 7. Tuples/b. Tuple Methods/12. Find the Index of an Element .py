# A Program to find the Index of an Element in a Tuple.

fruits = ("Apple", "Banana", "Mango", "Orange")

print(f"\nTuple: {fruits}")
fruit = input("Enter a fruit: ").title()

if fruit in fruits:
    print("Index:", fruits.index(fruit))
else:
    print("Fruit not found.")

# Explanation:
# The program uses the index() method to locate the first occurrence of an element in the tuple. If the element exists, its position is displayed. Checking whether the element exists before calling index() prevents a ValueError and makes the program more reliable.