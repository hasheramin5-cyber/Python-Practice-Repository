# a program to check if a number lies between 1 and 100 using conditional statements.

number = int(input("Enter a number: "))

if 1 <= number <= 100:
    print("The number lies between 1 and 100.")
else:
    print("The number is outside the range.")
    
# Explanation:
# The program prompts the user to input a number. It then uses a conditional statement (if, else) to check if the number lies between 1 and 100 (inclusive). The condition `1 <= number <= 100` checks if the number is greater than or equal to 1 and less than or equal to 100. If the condition is true, it prints that the number lies between 1 and 100; otherwise, it prints that the number is outside the range.