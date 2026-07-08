# A Program to remove all vowels from a string.

text = input("\nEnter a string: ")

result = ""

for character in text:
    if character.lower() not in "aeiou":
        result += character

print(f"String '{text}' without vowels is:", result)

# Explanation:
# The program loops through each character of the string. If the character is not a vowel (a, e, i, o, u), it is added to a new string. The final string without vowels is then displayed.