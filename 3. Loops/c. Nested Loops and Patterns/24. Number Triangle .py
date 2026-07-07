# A Program to print a number triangle.

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Explanation:
# The program prints a triangle of numbers using nested for loops. The outer loop controls the rows, while the inner loop prints numbers starting from 1 up to the current row number. Each row contains one more number than the previous row.