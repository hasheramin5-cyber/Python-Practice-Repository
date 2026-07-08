# A Program to check whether all characters in a string are digits.

text = input("\nEnter a string: ")

if text.isdigit():
    print("The string contains only digits.")
else:
    print("The string contains characters other than digits.")

# Explanation:
# The program checks whether every character in the string is a digit using the isdigit() method. If the string contains only numbers from 0 to 9, it returns True; otherwise, it returns False.