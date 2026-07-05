# What is Absolute Value?
# Absolute value is the distance of a number from zero on the number line, regardless of its sign. It is always a non-negative value. The absolute value of a number is denoted by two vertical bars surrounding the number, like this: |x|.

# What is abs(x)? The abs() function in Python is used to calculate the absolute value of a number. It takes a single argument (the number) and returns its absolute value. For example, abs(-5) will return 5, and abs(5) will also return 5.

# For example:
# |5| = 5 (the distance of 5 from 0 is 5)
# |-5| = 5 (the distance of -5 from 0 is also 5)

# a program to calculate the absolute value of a number using conditional statements.

number = float(input("Enter a number: "))

if number < 0:
    number = -number

print(f"Absolute value: {number}")

# Explanation:
# The program prompts the user to input a number. It then uses a conditional statement (if) to check if the number is negative. If the number is negative, it multiplies the number by -1 to make it positive. Finally, it prints the absolute value of the number. If the number is already non-negative, it simply prints the number as is.