# A Program to check whether an element exists in a list.

fruits = ["Apple", "Banana", "Mango", "Orange"]

fruit = input("\nEnter a fruit name: ").title()

if fruit in fruits:
    print(f"{fruit} exists in the list.")
else:
    print(f"{fruit} does not exist in the list.")

# Explanation:
# The program checks whether the entered fruit exists in the list using the 'in' operator. If the element is found, it displays a confirmation message; otherwise, it informs the user that the element is not present.