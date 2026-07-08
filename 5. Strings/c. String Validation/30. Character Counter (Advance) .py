# A Program to count uppercase letters, lowercase letters, digits, and special characters in a string.

text = input("\nEnter a string: ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

for character in text:
    if character.isupper():
        uppercase += 1
    elif character.islower():
        lowercase += 1
    elif character.isdigit():
        digits += 1
    else:
        special += 1
        
print("\nResults:")

print("Uppercase Letters :", uppercase)
print("Lowercase Letters :", lowercase)
print("Digits            :", digits)
print("Special Characters:", special)

# Explanation:
# The program examines every character in the string using a loop. It uses the built-in string methods isupper(), islower(), and isdigit() to classify each character. Any character that does not belong to these categories is counted as a special character. Finally, the program displays the total count for each category.