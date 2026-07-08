# A Program to check whether all characters in a string are alphabets.

text = input("\nEnter a string: ")

if text.isalpha():
    print("The string contains only alphabets.")
else:
    print("The string contains characters other than alphabets.")

# Explanation:
# The program checks whether every character in the string is an alphabet using the isalpha() method. If the string contains only letters (A-Z or a-z), the method returns True. If it contains numbers, spaces, or special characters, it returns False.