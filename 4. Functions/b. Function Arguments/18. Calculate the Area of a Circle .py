# A Program to calculate the area of a circle using a function.

def circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    print("Area =", area)

circle_area(7)

# Explanation:
# The program defines a function that calculates the area of a circle using the formula Area = π × r². The radius is passed as a parameter, and the function computes and displays the area. This example also demonstrates the use of the exponent operator (**) to calculate the square of the radius.