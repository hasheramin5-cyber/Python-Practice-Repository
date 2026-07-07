# A Program to print a right triangle pattern using asterisks (*).

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

# Explanation:
# The program prints a right triangle using nested for loops. The outer loop controls the number of rows, while the inner loop prints asterisks equal to the current row number. As the row number increases, one extra asterisk is printed, creating the triangle pattern.