# A Program to generate the Fibonacci series.

# What is Fibonacci series ?
# The Fibonacci series is a sequence of numbers in which each number is the sum of the two previous numbers.

# Example:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...


terms = int(input("\nEnter the number of terms: "))

first = 0
second = 1

for i in range(terms):
    print(first, end=" ")
    next_number = first + second
    first = second
    second = next_number

# Explanation:
# The program generates the Fibonacci series for the number of terms entered by the user. It starts with the first two numbers, 0 and 1, and each new number is calculated by adding the previous two numbers together. The process repeats until the required number of terms has been printed.