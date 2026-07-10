# A Program to Reverse a Tuple.

numbers = (10, 20, 30, 40, 50)

reversed_tuple = numbers[::-1]

print("\nOriginal Tuple:", numbers)
print("Reversed Tuple:", reversed_tuple)

# Explanation:
# The program reverses the tuple using slicing with a step value of -1. Since tuples are immutable, Python creates a new reversed tuple instead of modifying the original one. This demonstrates that many tuple operations produce new tuples rather than changing existing data.