# A Program to Sort a Tuple.

numbers = (45, 12, 89, 23, 67)

print(f"\nTuple: {numbers}")
sorted_tuple = tuple(sorted(numbers))

print("Sorted Tuple:", sorted_tuple)

# Explanation:
# The program uses the sorted() function to arrange the tuple elements in ascending order. Since sorted() returns a list, the result is converted back into a tuple using the tuple() function. Because tuples cannot be modified, Python creates a completely new sorted tuple.