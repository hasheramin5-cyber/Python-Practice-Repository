# Making a Simple Calculator in Python.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nAddition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")

if num2 != 0:
    print(f"Division: {num1 / num2}")
    print(f"Floor Division: {num1 // num2}")
    print(f"Modulus: {num1 % num2}")
else:
    print("Division by zero is not allowed.")