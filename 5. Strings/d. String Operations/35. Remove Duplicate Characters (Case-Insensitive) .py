# A Program to remove duplicate characters from a string without considering letter case.

text = input("\nEnter a string: ")

result = ""
seen = ""

for character in text:
    if character.lower() not in seen:
        seen += character.lower()
        result += character

print("After Removing Duplicates =", result)

# Explanation:
# The program removes duplicate characters without considering uppercase and lowercase letters as different. It keeps track of previously seen characters in lowercase using the variable 'seen'. If the lowercase version of a character has not been encountered before, the original character is added to the result. This preserves the original capitalization while removing duplicates in a case-insensitive manner.