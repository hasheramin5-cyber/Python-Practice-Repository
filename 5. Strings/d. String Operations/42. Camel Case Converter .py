# A Program to convert a sentence into camelCase.

# Definition:
# camelCase is a naming style in which the first word begins with a lowercase letter, and every following word starts with an uppercase letter without using spaces.

# Example:
# "hello world python" → "helloWorldPython"

sentence = input("\nEnter a sentence: ")

words = sentence.lower().split()

camel_case = words[0]

for word in words[1:]:
    camel_case += word.capitalize()

print("camelCase is:", camel_case)

# Explanation:
# The program converts the sentence into lowercase and splits it into individual words. The first word remains lowercase, while the first letter of every remaining word is capitalized using the capitalize() method. Finally, all the words are joined together without spaces to create a camelCase string.