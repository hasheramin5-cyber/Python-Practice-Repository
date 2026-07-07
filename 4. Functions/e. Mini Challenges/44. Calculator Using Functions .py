# A Program to perform basic arithmetic operations using functions.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Division by zero is not allowed."

number1 = float(input("\nEnter first number: "))
number2 = float(input("Enter second number: "))

print("\nResults: ")
print("Addition =", add(number1, number2))
print("Subtraction =", subtract(number1, number2))
print("Multiplication =", multiply(number1, number2))
print("Division =", divide(number1, number2))

# Explanation:
# The program defines separate functions for addition, subtraction, multiplication, and division. Each function performs a single task and returns its result. The main program calls these functions to perform calculations on the user's input.