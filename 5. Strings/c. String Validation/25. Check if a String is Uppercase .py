# A Program to check whether a string is completely uppercase.

text = input("\nEnter a string: ")

if text.isupper():
    print("The string is uppercase.")
else:
    print("The string is not uppercase.")

# Explanation:
# The program checks whether all alphabetic characters in the string are uppercase using the isupper() method. If any lowercase letter is present, the method returns False.