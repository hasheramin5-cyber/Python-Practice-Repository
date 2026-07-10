# A Program to access an Element of a Tuple using its Index.

fruits = ("Apple", "Banana", "Mango", "Orange")
print(f"\nTuple: {fruits}")

index = int(input("Enter the index: "))

if 0 <= index < len(fruits):
    print("Element:", fruits[index])
else:
    print("Invalid Index!")

# Explanation:
# The program asks the user for an index and retrieves the corresponding element from the tuple. Before accessing the element, it checks whether the index is valid to prevent an IndexError. Validating user input is an important habit because it makes programs more reliable and user-friendly.