# a program to determine if a triangle is valid using conditional statements.

side1 = float(input("\nEnter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
    
# Explanation:
# The program prompts the user to input the lengths of the three sides of a triangle. It then uses conditional statements (if, else) to check if the triangle is valid based on the triangle inequality theorem. The theorem states that the sum of the lengths of any two sides of a triangle must be greater than the length of the third side. If all three conditions are satisfied, it prints that the triangle is valid; otherwise, it prints that the triangle is not valid.