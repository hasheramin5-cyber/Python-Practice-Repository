# A Program to keep asking for a password until the correct password is entered.

correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter the password: ")

print("Access Granted!")

# Explanation:
# The program repeatedly asks the user to enter a password until the correct password is provided. It compares the entered password with the predefined correct password during each iteration of the while loop. Once the passwords match, the loop ends and the program displays a message confirming that access has been granted.