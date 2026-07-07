# A Program to print an inverted right triangle pattern using asterisks (*).

rows = 5

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Explanation:
# The program prints an inverted triangle using nested for loops. The outer loop starts from the maximum number of rows and decreases by one after each iteration. The inner loop prints the required number of asterisks for each row, producing the inverted triangle.