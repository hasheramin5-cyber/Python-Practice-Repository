# A Program to validate a person's name.

name = input("\nEnter your name: ").strip()

if name.replace(" ", "").isalpha():
    print("Valid User Name.")
else:
    print("Invalid User Name.")

# Explanation:
# The program checks whether the entered name contains only alphabetic characters and spaces. First, it removes any leading and trailing whitespace using the strip() method. Then, it removes all spaces between words using the replace() method and uses isalpha() to verify that the remaining characters are all letters. If the condition is satisfied, the name is considered valid; otherwise, it is considered invalid.