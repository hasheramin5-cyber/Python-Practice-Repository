# A Program to simulate a simple shopping cart.

cart = []

while True:
    item = input("Enter an item (or 'done' to finish): ")

    if item.lower() == "done":
        break

    cart.append(item)

print("\nShopping Cart:", cart)

# Explanation:
# The program allows the user to continuously add items to a shopping cart until they choose to stop. Each entered item is stored in a list using the append() method. This demonstrates how lists are used in e-commerce websites and inventory systems to store collections of products dynamically.