# A Program to add multiple elements to a list using the extend() method.

numbers = [10, 20, 30]

print("\nBefore Updating List is:", numbers)

numbers.extend([40, 50, 60])

print("After Updating List is:", numbers)

# Explanation:
# The program adds multiple elements to the end of a list using the extend() method. Unlike append(), which adds a single element, extend() adds every element from another iterable individually.