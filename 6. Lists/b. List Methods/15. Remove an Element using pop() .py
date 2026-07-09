# A Program to remove an element from a specific index using the pop() method.

numbers = [10, 20, 30, 40, 50]

index = int(input("\nEnter the index to remove: "))

print("List:", numbers)

if 0 <= index < len(numbers):
    removed = numbers.pop(index)
    print("\nRemoved Element =", removed)
    print("Updated List:", numbers)
else:
    print("Invalid Index!")

# Explanation:
# The program removes an element from the specified index using the pop() method. Unlike remove(), pop() removes an element by its position and also returns the removed element.