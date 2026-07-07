# A Program to return whether a number is even.

def is_even(number):
    return number % 2 == 0

result = is_even(12)

if result:
    print("The number is Even.")
else:
    print("The number is Odd.")

# Explanation:
# The program defines a function that checks whether a number is even. If the number is divisible by 2, the function returns True; otherwise, it returns False. The returned Boolean value is then used in an if-else statement to display the appropriate message.