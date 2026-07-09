# A Program to find the number of records in a nested list.

students = [
    ["Ali", 20],
    ["Sara", 21],
    ["Ahmed", 19]
]

print(f"\nList: {students}")
print("Total Records:", len(students))

# Explanation:
# The program uses the len() function to count how many inner lists are stored in the nested list. Since each inner list represents one record, the result indicates the total number of records. Later, you'll learn how to count both rows and columns in multidimensional data.