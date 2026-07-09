# A Program to find the index of an element in a list.

animals = ["Cat", "Dog", "Rabbit", "Horse"]

animal = input("\nEnter an animal: ").title()

if animal in animals:
    print(f"Index of {animal} is {animals.index(animal)}.")
else:
    print("Animal not found.")

# Explanation:
# The program finds the position of an element using the index() method. If the element exists, its index is displayed; otherwise, an appropriate message is shown.