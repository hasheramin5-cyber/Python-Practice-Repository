# A Program to print every element of a nested list.

students = [
    ["Ali", 20],
    ["Sara", 21],
    ["Ahmed", 19]
]

for student in students:
    for detail in student:
        print(detail)

# Explanation:
# The program uses nested for loops. The outer loop accesses each student record, while the inner loop accesses every individual value within that record. Nested loops are commonly used with nested lists because they allow you to process every element one by one. This concept is essential for working with tables, matrices, and multidimensional datasets.