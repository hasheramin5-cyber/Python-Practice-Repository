# A Program to split a string into a list of words.

sentence = input("\nEnter a sentence: ")

words = sentence.split()

print("Words =", words)

# Explanation:
# The program uses the split() method to divide a sentence into individual words. By default, split() separates the string wherever it finds a space and stores the words in a list.