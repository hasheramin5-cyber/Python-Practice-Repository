# A Program to count the number of words in a sentence.

sentence = input("\nEnter a sentence: ")

words = sentence.split()

print("Number of Words =", len(words))

# Explanation:
# The program splits the sentence into individual words using the split() method. The len() function is then used to count how many words are present in the resulting list.