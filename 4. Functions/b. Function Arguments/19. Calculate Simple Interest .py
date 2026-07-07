# A Program to calculate simple interest using a function.

def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    print("Simple Interest =", interest)

simple_interest(10000, 5, 2)

# Explanation:
# The program defines a function that calculates simple interest using the formula (Principal × Rate × Time) ÷ 100. It accepts the principal amount, interest rate, and time period as parameters. After performing the calculation, the function displays the simple interest.