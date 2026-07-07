# A Program to return the largest of two numbers using a function.

def largest(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2

result = largest(45, 82)
print("Largest Number =", result)

# Explanation:
# The program defines a function that compares two numbers and returns the larger one. It uses an if-else statement to determine which value is greater. The returned value is stored in a variable and displayed outside the function.