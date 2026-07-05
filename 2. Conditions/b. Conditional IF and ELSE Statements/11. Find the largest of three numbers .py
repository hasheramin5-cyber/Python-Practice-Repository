# a program to find the largest of three numbers using conditional statements.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")
    
# Explanation:
# The program prompts the user to input three numbers. It then uses conditional statements (if, elif, else) to compare the three numbers and determine which one is the largest. The program checks if the first number is greater than or equal to both the second and third numbers. If true, it prints that the first number is the largest. If not, it checks if the second number is greater than or equal to both the first and third numbers. If true, it prints that the second number is the largest. If neither of those conditions are met, it concludes that the third number must be the largest and prints that result.