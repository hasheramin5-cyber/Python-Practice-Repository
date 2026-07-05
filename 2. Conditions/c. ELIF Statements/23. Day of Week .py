# a program to print the day of the week based on a number input using conditional statements.

day = int(input("Enter a number (1-7): "))

if day == 1:
    print("Day is Monday.")
elif day == 2:
    print("Day is Tuesday.")
elif day == 3:
    print("Day is Wednesday.")
elif day == 4:
    print("Day is Thursday.")
elif day == 5:
    print("Day is Friday.")
elif day == 6:
    print("Day is Saturday.")
elif day == 7:
    print("Day is Sunday.")
else:
    print("Invalid day number.")
    
# Explanation:
# The program prompts the user to input a number representing a day of the week (1 for Monday, 2 for Tuesday, and so on). It then uses conditional statements (if, elif, else) to check the value of the input number and print the corresponding day of the week. If the input number is not between 1 and 7, it prints "Invalid day number."