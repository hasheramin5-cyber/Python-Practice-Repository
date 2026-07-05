# A Basic Calculator Program Using User Choice.

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Choose an operation (1-4): "))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid choice.")
 
    
# Explanation:
# The program prompts the user to input two numbers. It then presents a menu of operations (addition, subtraction, multiplication, division) and asks the user to choose one. Based on the user's choice, it performs the corresponding arithmetic operation using conditional statements (if, elif, else). If the user chooses division, it checks if the second number is not zero to avoid division by zero errors. If the user enters an invalid choice, it prints an error message.