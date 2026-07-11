# A Program to Remove Duplicate Elements from a Tuple.

numbers = (10, 20, 30, 20, 40, 10, 50)

unique_tuple = tuple(set(numbers))

print("\nOriginal Tuple:", numbers)
print("Tuple Without Duplicates:", unique_tuple)

# Explanation:
# Since tuples are immutable, duplicates cannot be removed directly. The program first converts the tuple into a set, which automatically removes duplicate values. It then converts the set back into a tuple. Keep in mind that sets do not preserve the original order of elements, so the resulting tuple may appear in a different order.