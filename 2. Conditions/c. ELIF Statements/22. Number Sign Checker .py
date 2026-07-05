# a program to check the sign of a number using conditional statements.

number = float(input("Enter a number: "))

if number > 0:
    print(number, "is a Positive Number.")
elif number < 0:
    print(number, "is a Negative Number.")
else:
    print(number, "is Zero.")
    
# Explanation:
# The program prompts the user to input a number. It then uses conditional statements (if, elif, else) to check the sign of the number. If the number is greater than zero, it prints "Positive Number.". If the number is less than zero, it prints "Negative Number.". If the number is equal to zero, it prints "The Number is Zero."