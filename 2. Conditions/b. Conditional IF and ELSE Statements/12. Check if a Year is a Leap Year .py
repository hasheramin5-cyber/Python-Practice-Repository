# a program to check if a year is a leap year using conditional statements.

year = int(input("\nEnter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
       
# Explanation:
# The program prompts the user to input a year. It then uses conditional statements (if, else) to check if the year is a leap year. A year is a leap year if it is divisible by 400 or if it is divisible by 4 but not by 100. If either of these conditions is true, the program prints that the year is a leap year; otherwise, it prints that the year is not a leap year.