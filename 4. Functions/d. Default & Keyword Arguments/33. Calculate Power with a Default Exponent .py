# A Program to calculate the power of a number using a default exponent.

def power(base, exponent=2):
    print("Result =", base ** exponent)

power(5)
power(5, 3)

# Explanation:
# The program defines a function that calculates the power of a number. By default, the exponent is set to 2, so the function calculates the square of a number unless another exponent is provided. This allows the same function to perform multiple related tasks.