# A Program to Print the Multiplication Table of the Number Given by the User.

number = int(input("\nEnter a number: "))

print(f"\nTable of {number}")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

