# A Program to check whether a string is alphanumeric.

# What does Alphanumeric mean?
# Alphanumeric means a string contains only letters (A–Z, a–z) and numbers (0–9).i.e.,
# Letters are allowed.
# Numbers are allowed.
# Spaces are not allowed.
# Special characters like @, #, _, !, $, % are not allowed.


text = input("\nEnter a string: ")

if text.isalnum():
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")

# Explanation:
# The program checks whether the string contains only letters and numbers using the isalnum() method. Spaces and special characters are not allowed for the method to return True.