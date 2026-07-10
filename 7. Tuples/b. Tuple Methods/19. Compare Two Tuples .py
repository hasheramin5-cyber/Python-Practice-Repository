# A Program to compare two tuples.

tuple1 = (10, 20, 30)
tuple2 = (10, 20, 30)

print(f"\nTuple1: {tuple1}\nTuple2: {tuple2}")

if tuple1 == tuple2:
    print("Both tuples are equal.")
else:
    print("The tuples are not equal.")

# Explanation:
# The program compares two tuples using the equality operator (==). Two tuples are considered equal only if they contain the same elements in the same order. Tuple comparison is useful when validating stored data, checking configurations, or verifying whether two records contain identical information.