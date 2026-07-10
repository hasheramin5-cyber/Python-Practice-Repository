# A Program to concatenate two tuples.

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

print(f"\nTuple1: {tuple1}\nTuple2: {tuple2}")
combined_tuple = tuple1 + tuple2

print("Combined Tuple:", combined_tuple)

# Explanation:
# The program joins two tuples together using the + operator. Instead of modifying the original tuples, Python creates a new tuple containing all elements from both tuples. Concatenation is commonly used to combine related datasets while keeping the original tuples unchanged.