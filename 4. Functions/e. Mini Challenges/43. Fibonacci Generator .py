# A Program to generate the Fibonacci series using a function.

# Definition:
# The Fibonacci series is a sequence of numbers where each number is the sum of the two previous numbers. It starts with 0 and 1.

def fibonacci(terms):
    first = 0
    second = 1

    for i in range(terms):
        print(first, end=" ")
        next_number = first + second
        first = second
        second = next_number

number = int(input("\nEnter the number of terms: "))
fibonacci(number)

# Explanation:
# The program defines a function that generates the Fibonacci series. Starting with 0 and 1, each new number is calculated by adding the previous two numbers together. The function prints the sequence up to the number of terms entered by the user.