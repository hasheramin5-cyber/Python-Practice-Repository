# A Program to print a rectangle pattern using asterisks (*).

rows = 3
columns = 5

for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print()

# Explanation:
# The program uses nested for loops to print a rectangle of asterisks. The outer loop controls the number of rows, while the inner loop prints the required number of asterisks in each row. The end="" parameter keeps the asterisks on the same line, and print() moves the cursor to the next line after each row is completed.