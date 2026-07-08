# A Program to remove leading and trailing whitespace from a string.

text = input("Enter a string: ")

print("Trimmed String =", text.strip())

# Explanation:
# The program removes any spaces, tabs, or newline characters from the beginning and end of the string using the strip() method. It does not remove spaces that appear between words.