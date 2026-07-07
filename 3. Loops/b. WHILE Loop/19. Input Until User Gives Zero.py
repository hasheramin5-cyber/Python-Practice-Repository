# A Program to keep asking the user for input until 0 is entered.

number = -1

while number != 0:
    number = int(input("Enter a number (0 to stop): "))

print("Program Ended.")

# Explanation:
# The program repeatedly asks the user to enter a number using a while loop. The loop continues as long as the entered value is not 0. When the user finally enters 0, the loop condition becomes False, the loop stops, and the program displays a message indicating that it has ended.