# A Program to remove duplicate characters from a string.

text = input("\nEnter a string: ")

result = ""

for character in text:
    if character not in result:
        result += character

print("After Removing Duplicates =", result)

# Explanation:
# The program removes duplicate characters while keeping their first occurrence. It checks each character one by one and adds it to a new string only if it has not already been added.