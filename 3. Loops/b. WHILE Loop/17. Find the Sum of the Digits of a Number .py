# A Program to find the sum of the digits of a number.

number = abs(int(input("\nEnter a number: ")))

total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print("Sum of Digits =", total)

# Explanation:
# The program calculates the sum of all digits in a number using a while loop. It extracts one digit at a time using the modulus operator and adds it to the variable 'total'. After removing the processed digit using floor division, the loop continues until all digits have been added together, and the final sum is displayed.