# A Program to add a new record to a nested list.

students = [
    ["Ali", 20],
    ["Sara", 21]
]

students.append(["Ahmed", 19])

print("\nList:",students)

# Explanation:
# The program adds a completely new inner list using the append() method. Instead of adding a single value, an entire record is inserted into the nested list. This technique is widely used when adding new users, products, employees, or other structured records in real-world applications.