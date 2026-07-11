# A Program to demonstrate immutable and mutable objects.

tuple_data = (10, 20, 30)
list_data = [10, 20, 30]

print(f"\nTuple Data: {tuple_data}")
print(f"List Data: {list_data}")

list_data[0] = 100

print("Tuple:", tuple_data)
print("Modified List:", list_data)

# Explanation:
# The program compares an immutable object (tuple) with a mutable object (list). The list allows its elements to be changed after creation, so the first value is successfully updated from 10 to 100. The tuple remains unchanged because tuples are immutable. This difference is one of the main reasons developers choose tuples for storing fixed data and lists for storing data that may change during program execution.