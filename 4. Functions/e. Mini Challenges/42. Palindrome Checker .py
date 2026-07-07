# A Program to check whether a string is a palindrome using a function.

# Definition:
# A palindrome is a word, number, or sentence that reads the same forward and backward, such as "madam" or "level".

def is_palindrome(text):
    reverse = ""

    for character in text:
        reverse = character + reverse

    return text.lower() == reverse.lower()

word = input("\nEnter a word: ")

if is_palindrome(word):
    print("Palindrome.")
else:
    print("Not a Palindrome.")

# Explanation:
# The program defines a function that reverses a string and compares it with the original string. If both strings are identical, the function returns True; otherwise, it returns False. The returned value is then used to determine whether the entered word is a palindrome.