# A Program to find the longest word in a sentence.

sentence = input("\nEnter a sentence: ")

words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word is:", longest)

# Explanation:
# The program separates the sentence into words and assumes the first word is the longest. It then compares each remaining word with the current longest word. Whenever a longer word is found, it becomes the new longest word.