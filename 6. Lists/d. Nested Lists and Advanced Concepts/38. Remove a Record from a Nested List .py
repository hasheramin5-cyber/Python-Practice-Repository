# A Program to remove a record from a nested list.

students = [
    ["Ali", 20],
    ["Sara", 21],
    ["Ahmed", 19]
]

students.pop(1)

print("List:", students)

# Explanation:
# The program removes one complete record from the nested list using the pop() method. Since each inner list represents a single record, removing one inner list is similar to deleting an entire row from a table or spreadsheet. This operation is common in data management applications.