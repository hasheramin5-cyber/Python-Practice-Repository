# A Program to print an inverted pyramid pattern using asterisks (*).

rows = 5

for i in range(rows):
    for j in range(i):
        print(" ", end="")
    for k in range(2 * (rows - i) - 1):
        print("*", end="")
    print()

# Explanation:
# The program prints an inverted pyramid using nested for loops. The first inner loop prints leading spaces, while the second inner loop prints the required number of asterisks. As the rows progress, the spaces increase and the number of asterisks decreases, creating an inverted pyramid.