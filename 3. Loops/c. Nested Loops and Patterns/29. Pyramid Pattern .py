# A Program to print a pyramid pattern using asterisks (*).

rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

# Explanation:
# The program prints a pyramid using nested for loops. The first inner loop prints the required spaces before each row, while the second inner loop prints the asterisks. As the rows increase, the spaces decrease and the number of asterisks increases, forming a pyramid.