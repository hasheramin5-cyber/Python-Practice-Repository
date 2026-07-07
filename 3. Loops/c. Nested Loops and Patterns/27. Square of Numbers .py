# A Program to print a square pattern of numbers.

rows = 5

for i in range(1, rows + 1):
    for j in range(rows):
        print(i, end="")
    print()

# Explanation:
# The program prints a square pattern where each row contains the same number repeated multiple times. The outer loop controls the current number to print, while the inner loop repeats that number across the row, creating a square-shaped pattern.