# A Program to Search for an Element in a Tuple.

fruits = ("Apple", "Banana", "Mango", "Orange")

print(f"\nTuple: {fruits}")
fruit = input("\nEnter a fruit to search: ").title()

if fruit in fruits:
    print(f"{fruit} found in the Tuple.")
else:
    print(f"{fruit} not found in the Tuple.")

# Explanation:
# The program searches for an element using Python's membership operator (in). Instead of manually checking every element, Python performs the search and returns either True or False. Membership testing is widely used for validation, searching, and access control in real-world applications.