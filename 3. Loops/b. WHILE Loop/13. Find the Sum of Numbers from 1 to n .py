# A Program to find the sum of numbers from 1 to n using a while loop.

n = int(input("\nEnter a positive number: "))

total = 0
number = 1

while number <= n:
    total += number
    number += 1

print("Sum =", total)

# Explanation:
# The program asks the user to enter a positive number and calculates the sum of all numbers from 1 to that number. It uses a while loop to repeatedly add each number to the variable 'total'. The loop continues until all numbers from 1 to n have been added, and then the final sum is displayed.