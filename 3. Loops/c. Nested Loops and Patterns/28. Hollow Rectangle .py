# A Program to print a hollow rectangle pattern.

rows = 5
columns = 8

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Explanation:
# The program prints a hollow rectangle using nested for loops and conditional statements. Asterisks are printed only on the first row, last row, first column, and last column. All other positions contain spaces, creating a hollow shape.