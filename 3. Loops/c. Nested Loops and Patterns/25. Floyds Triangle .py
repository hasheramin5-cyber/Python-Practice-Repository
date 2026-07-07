# A Program to print Floyd's Triangle.

rows = 4
number = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()

# Explanation:
# The program prints Floyd's Triangle using nested for loops. A variable named 'number' starts at 1 and increases after every print operation. The outer loop controls the rows, while the inner loop prints consecutive numbers, forming Floyd's Triangle.