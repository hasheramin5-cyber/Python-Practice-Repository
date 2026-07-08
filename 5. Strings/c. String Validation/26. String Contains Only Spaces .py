# A Program to check whether a string contains only whitespace characters.

text = input("\nEnter a string: ")

if text.isspace():
    print("The string contains only spaces.")
else:
    print("The string contains characters other than spaces.")

# Explanation:
# The program checks whether the string contains only whitespace characters using the isspace() method. Whitespace includes spaces, tabs, and newline characters. If any visible character exists, the method returns False.