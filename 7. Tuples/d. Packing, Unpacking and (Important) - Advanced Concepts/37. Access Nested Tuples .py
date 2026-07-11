# A Program to Access Elements from a Nested Tuple.

students = (
    ("Hasher", 20),
    ("Ali", 22),
    ("Sara", 21)
)

print("\nStudent Name:", students[1][0])
print("Student Age:", students[1][1])

# Explanation:
# The program accesses data from a nested tuple using multiple indexes. The first index selects the required inner tuple, while the second index selects the required element inside that tuple. This approach allows Python to work with structured data stored in multiple levels.