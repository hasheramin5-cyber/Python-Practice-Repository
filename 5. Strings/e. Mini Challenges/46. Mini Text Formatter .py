# A Program to format text using different string methods.

text = input("\nEnter a sentence: ")

print("\nResults:")

print("Uppercase :", text.upper())
print("Lowercase :", text.lower())
print("Title Case:", text.title())
print("Swap Case :", text.swapcase())
print("Trimmed   :", text.strip())

# Explanation:
# The program demonstrates several commonly used string methods. It displays the entered text in uppercase, lowercase, title case, swapped case, and also removes any leading or trailing whitespace using the strip() method.