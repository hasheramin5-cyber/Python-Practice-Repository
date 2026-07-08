# A Program to check the strength of a password.

# Definition:
# A strong password should contain at least one uppercase letter, one lowercase letter, one digit, one special character, and should be at least 8 characters long.

password = input("\nEnter a password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for character in password:
    if character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif character.isdigit():
        has_digit = True
    else:
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong Password.")
else:
    print("Weak Password.")

# Explanation:
# The program checks whether the password satisfies common security requirements. It verifies the presence of uppercase letters, lowercase letters, digits, and special characters, along with a minimum length of eight characters. If all conditions are met, the password is considered strong.