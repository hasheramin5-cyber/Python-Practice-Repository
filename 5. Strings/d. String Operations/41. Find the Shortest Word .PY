# A Program to find the shortest word in a sentence.

sentence = input("\nEnter a sentence: ")

words = sentence.split()

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest Word is:", shortest)

# Explanation:
# The program separates the sentence into words and assumes the first word is the shortest. It then compares every remaining word with it. Whenever a shorter word is found, it replaces the previous shortest word.