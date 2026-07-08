# A Program to check whether a password contains at least one digit.

password = input("\nEnter a password: ")

has_digit = False

for character in password:
    if character.isdigit():
        has_digit = True
        break

if has_digit:
    print("Password contains at least one number.")
else:
    print("Password does not contain any numbers.")

# Explanation:
# The program checks each character of the password using a loop. If it finds a digit, it sets a flag to True and stops checking further. The result determines whether the password contains at least one numeric character.