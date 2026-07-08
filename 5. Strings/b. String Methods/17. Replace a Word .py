# A Program to replace a word in a string.

text = input("\nEnter a sentence: ")

old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

print("\nUpdated Sentence =", text.replace(old_word, new_word))

# Explanation:
# The program replaces every occurrence of a specified word with a new word using the replace() method. The updated string is then displayed without changing the original string variable.