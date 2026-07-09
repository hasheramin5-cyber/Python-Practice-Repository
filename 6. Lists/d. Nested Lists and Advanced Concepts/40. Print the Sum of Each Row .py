# A Program to calculate the sum of each row in a matrix.

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for row in matrix:
    print("\n")
    print("Row:", row)
    print("Sum =", sum(row))

# Explanation:
# The program processes one row of the matrix at a time and calculates its total using the sum() function. Each row is itself a list, making it possible to apply list operations to every row individually. This concept is widely used in data analysis, spreadsheets, scientific computing, and machine learning when performing calculations on tabular data.