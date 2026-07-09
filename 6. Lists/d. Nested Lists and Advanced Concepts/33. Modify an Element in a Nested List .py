# A Program to modify an element in a nested list.

students = [
    ["Ali", 20],
    ["Sara", 21],
    ["Ahmed", 19]
]

students[0][1] = 22

print("\nList:", students)

# Explanation:
# The program updates an existing value inside a nested list. Here, the age of the first student is changed from 20 to 22. Since lists are mutable, individual elements can be modified without creating a new list. This is useful when updating records in applications such as student management systems or inventory systems.