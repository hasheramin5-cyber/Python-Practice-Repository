# a program to check if a number is divisible by 3 and 5 using conditional statements.

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5.")
else:
    print(f"{number} is not divisible by both 3 and 5.")
    
# Explanation:
# The program prompts the user to input a number. It then uses conditional statements (if, else) to check if the number is divisible by both 3 and 5. The program uses the modulo operator (%) to determine the remainder when the number is divided by 3 and 5. If the remainder is zero for both divisions, it prints that the number is divisible by both 3 and 5; otherwise, it prints that the number is not divisible by both 3 and 5.