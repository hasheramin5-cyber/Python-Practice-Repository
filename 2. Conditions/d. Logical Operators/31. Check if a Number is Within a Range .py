# a program to check if a number is within a specified range using logical operators.

number = int(input("Enter a number: "))

if number >= 10 and number <= 100:
    print("The number is within the range.")
else:
    print("The number is outside the range.")
    
# Explanation:
# The program prompts the user to input a number. It then uses a conditional statement (if, else) to check if the number is within the range of 10 to 100 (inclusive). The condition `number >= 10 and number <= 100` checks if the number is greater than or equal to 10 and less than or equal to 100. If the condition is true, it prints that the number is within the range; otherwise, it prints that the number is outside the range.