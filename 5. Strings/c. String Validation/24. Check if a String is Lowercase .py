# A Program to check whether a string is completely lowercase.

text = input("\nEnter a string: ")

if text.islower():
    print("The string is lowercase.")
else:
    print("The string is not lowercase.")

# Explanation:
# The program checks whether all alphabetic characters in the string are lowercase using the islower() method. If even one uppercase letter exists, the method returns False.