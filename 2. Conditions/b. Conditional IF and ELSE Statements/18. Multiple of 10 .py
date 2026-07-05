# a program to check if a number is a multiple of 10 using conditional statements.

number = int(input("Enter a number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
    
# Explanation:
# The program prompts the user to input a number. It then uses a conditional statement (if, else) to check if the number is a multiple of 10. The program uses the modulo operator (%) to determine the remainder when the number is divided by 10. If the remainder is zero, it prints that the number is a multiple of 10; otherwise, it prints that the number is not a multiple of 10.