# A Program to generate a Simple Shopping Receipt.

items = (
    ("Milk", 180),
    ("Bread", 120),
    ("Eggs", 300)
)

total = 0

print("Shopping Receipt\n")

for item, price in items:
    print(f"{item}: Rs.{price}")
    total += price

print("----------------")
print("Total:", total)

# Explanation:
# The program stores shopping items and their prices as nested tuples. During each iteration, the item name and price are unpacked into separate variables. The price is added to the variable 'total', which keeps track of the overall bill. After all items have been processed, the final amount is displayed.