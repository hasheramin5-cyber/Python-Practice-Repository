# A Program to divide two numbers using a function.

def divide(number1, number2):
    if number2 != 0:
        print("Quotient =", number1 / number2)
    else:
        print("Division by zero is not allowed.")

divide(20, 5)

# Explanation:
# The program defines a function that divides one number by another. Before performing the division, it checks whether the second number is zero because division by zero is not allowed in mathematics or Python. If the divisor is valid, the quotient is displayed; otherwise, an appropriate message is shown.