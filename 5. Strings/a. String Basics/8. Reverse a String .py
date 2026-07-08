# A Program to reverse a string.

text = input("\nEnter a string: ")

reverse = text[::-1]

print("Reversed String =", reverse)

# Explanation:
# The program reverses a string using Python's slicing technique. The slice [::-1] starts from the end of the string and moves backward one character at a time, producing the reversed version of the original string.