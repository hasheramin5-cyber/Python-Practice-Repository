# A Program to print numbers from 1 to n using a function.

def print_numbers(n):
    for number in range(1, n + 1):
        print(number)

print_numbers(10)

# Explanation:
# The program defines a function that accepts a number 'n' as a parameter and prints all numbers from 1 to that value using a for loop. The function becomes reusable because different values of 'n' can be provided whenever it is called, allowing it to print different ranges of numbers.