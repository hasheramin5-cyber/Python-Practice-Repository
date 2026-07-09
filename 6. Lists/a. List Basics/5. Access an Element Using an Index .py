# A Program to access an element of a list using an index.

cities = ["Lahore", "Karachi", "Islamabad", "Peshawar", "Quetta"]

index = int(input("Enter the index: "))

if 0 <= index < len(cities):
    print("Element =", cities[index])
else:
    print("Invalid Index!")

# Explanation:
# The program asks the user to enter an index number and retrieves the corresponding element from the list. Before accessing the element, it checks whether the entered index is within the valid range to prevent an IndexError.