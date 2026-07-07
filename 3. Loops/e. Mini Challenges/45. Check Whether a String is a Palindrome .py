# A Program to check whether a string is a palindrome.

# What is Palindrome ?
# A palindrome is a word, number, or sentence that reads the same forward and backward.

# Example:

# madam      → Palindrome
# level      → Palindrome
# hello      → Not a Palindrome


text = input("Enter a string: ").lower()

reverse = ""

for character in text:
    reverse = character + reverse

if text == reverse:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")
   

# Explanation:
# The program checks whether a string reads the same forwards and backwards. It first creates a reversed version of the string using a loop and then compares it with the original string. If both strings are identical, the string is a palindrome; otherwise, it is not.