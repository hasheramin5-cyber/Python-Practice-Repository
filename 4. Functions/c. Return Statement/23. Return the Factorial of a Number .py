# A Program to return the factorial of a number using a function.

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

answer = factorial(5)
print("Factorial =", answer)

# Explanation:
# The program defines a function that calculates the factorial of a number using a loop. The function multiplies all numbers from 1 up to the given number and returns the final result. The returned value is stored in a variable and then displayed outside the function.