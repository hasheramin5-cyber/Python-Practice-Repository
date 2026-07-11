# Real-Life Use of Nested Tuple:
# Nested tuples are commonly used to store records where each record contains multiple related values. For example, a school can store each student's name and age, a hospital can store patient records, a company can store employee details, or an online store can store product information. Since tuples are immutable, they are a good choice when these records should remain unchanged during program execution.
# Example:
'''
patients = (
    ("Ahmed", 32, "Fever"),
    ("Sara", 28, "Diabetes"),
    ("Ali", 45, "Fracture")
)

'''

# A Program to Create a Nested Tuple.

students = (
    ("Hasher", 20),
    ("Ali", 22),
    ("Sara", 21)
)

print("\nNested Tuple:")
print(students)

# Explanation:
# The program creates a nested tuple. Instead of storing simple values, each element of the main tuple is itself another tuple. Nested tuples are useful for organizing related information, such as student records, coordinates, product details, and database-like structures.