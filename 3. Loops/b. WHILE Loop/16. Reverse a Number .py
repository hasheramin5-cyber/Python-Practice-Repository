# A Program to reverse a number using a while loop.

number = int(input("\nEnter a number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reversed Number =", reverse)

# Explanation:
# The program reverses a number using a while loop. During each iteration, it extracts the last digit of the number using the modulus operator, adds it to the reversed number after shifting the existing digits one place to the left, and removes the last digit from the original number using floor division. This process continues until all digits have been processed, and the reversed number is displayed.