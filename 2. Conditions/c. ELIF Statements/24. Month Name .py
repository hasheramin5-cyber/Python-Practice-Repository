# A Program to print the month name based on a number input using conditional statements.

month = int(input("Enter month number (1-12): "))

if month == 1:
    print("The Month is January.")
elif month == 2:
    print("The Month is February.")
elif month == 3:
    print("The Month is March.")
elif month == 4:
    print("The Month is April.")
elif month == 5:
    print("The Month is May.")
elif month == 6:
    print("The Month is June.")
elif month == 7:
    print("The Month is July.")
elif month == 8:
    print("The Month is August.")
elif month == 9:
    print("The Month is September.")
elif month == 10:
    print("The Month is October.")
elif month == 11:
    print("The Month is November.")
elif month == 12:
    print("The Month is December.")
else:
    print("Invalid month number.")

    
# Explanation:
# The program prompts the user to input a number representing a month (1 for January, 2 for February, and so on). It then uses conditional statements (if, elif, else) to check the value of the input number and print the corresponding month name. If the input number is not between 1 and 12, it prints "Invalid month number."