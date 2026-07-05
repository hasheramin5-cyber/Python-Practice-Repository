# A Program to find the largest number among three numbers entered by the user.

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest.")
else:
    print(f"{num3} is the largest.")
    
# Explanation:
# The code finds the largest number among three numbers entered by the user. The user is prompted to input three numbers. The program then compares the numbers using logical operators to determine which one is the largest. It prints the largest number accordingly.