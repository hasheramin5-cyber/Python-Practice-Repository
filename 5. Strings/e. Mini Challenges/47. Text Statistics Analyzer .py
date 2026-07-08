# A Program to analyze text statistics.

text = input("\nEnter a paragraph: ")

characters = len(text)
words = len(text.split())
sentences = text.count(".") + text.count("!") + text.count("?")

print("\nResults:")

print("Characters :", characters)
print("Words      :", words)
print("Sentences  :", sentences)

# Explanation:
# The program analyzes a paragraph by calculating the total number of characters, words, and sentences. It uses the len() function, split() method, and count() method to generate the statistics.