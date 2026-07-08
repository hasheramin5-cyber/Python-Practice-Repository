# A Program to find the most frequent character in a string.

text = input("\nEnter a string: ")

maximum_character = ""
maximum_count = 0

for character in text:
    count = text.count(character)

    if count > maximum_count:
        maximum_count = count
        maximum_character = character

print("Most Frequent Character =", maximum_character)
print("Occurrences =", maximum_count)

# Explanation:
# The program checks how many times each character appears in the string using the count() method. It keeps track of the character with the highest occurrence and finally displays the most frequent character along with its total count.