# a program to check if a character is uppercase or lowercase using conditional statements.

character = input("Enter a character: ")

if character.isupper():
    print("Uppercase letter.")
else:
    print("Lowercase letter.")
    
# Explanation:
# The program prompts the user to input a character. It then uses a conditional statement (if, else) to check if the character is an uppercase letter or a lowercase letter. The `isupper()` method is used to determine if the character is uppercase. If the character is uppercase, it prints "Uppercase letter."; otherwise, it prints "Lowercase letter."