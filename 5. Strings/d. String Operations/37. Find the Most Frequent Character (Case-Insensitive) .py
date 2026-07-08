# A Program to find the most frequent character(s) in a string without considering letter case.

text = input("\nEnter a string: ").lower()

maximum_count = 0

for character in text:
    if character != " ":
        count = text.count(character)

        if count > maximum_count:
            maximum_count = count

printed = ""

print("Most Frequent Character(s):", end=" ")

for character in text:
    if character != " " and text.count(character) == maximum_count:
        if character not in printed:
            print(character, end=" ")
            printed += character

print("\nOccurrences =", maximum_count)

# Explanation:
# The program first converts the string to lowercase so that uppercase and lowercase letters are treated as the same character. It finds the highest occurrence count and then prints every character whose frequency matches that highest count. Duplicate characters are avoided by keeping track of the characters that have already been printed.