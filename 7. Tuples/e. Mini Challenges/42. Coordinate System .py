# A Program to store and display Coordinate Points.

points = (
    (2, 5),
    (4, 8),
    (7, 3),
    (9, 6)
)

print("Coordinate Points:\n")

for x, y in points:
    print(f"({x}, {y})")

# Explanation:
# The program stores multiple coordinate points inside a nested tuple. Each inner tuple contains an x-coordinate and a y-coordinate. The for loop unpacks every coordinate into the variables 'x' and 'y' before printing them. Tuples are commonly used for coordinates because the values usually remain fixed throughout the execution of a program.