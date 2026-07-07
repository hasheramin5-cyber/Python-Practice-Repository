# A Program to print the multiplication table of a number using a while loop.

number = int(input("\nEnter a number: "))
print(f"\nTable of {number}")

i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

# Explanation:
# The program prompts the user to enter a number and prints its multiplication table from 1 to 10 using a while loop. The variable 'i' starts from 1 and increases after every iteration until it reaches 10. During each iteration, the entered number is multiplied by the current value of 'i' and the result is displayed.