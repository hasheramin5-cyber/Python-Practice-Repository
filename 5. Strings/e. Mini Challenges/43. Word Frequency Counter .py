# A Program to count the frequency of each word in a sentence.

sentence = input("\nEnter a sentence: ").lower()

words = sentence.split()

counted_words = []

for word in words:
    if word not in counted_words:
        print(f"{word} : {words.count(word)}")
        counted_words.append(word)

# Explanation:
# The program converts the sentence into lowercase and splits it into individual words. It then checks each word and prints its frequency using the count() method. A separate list is used to ensure that each word is displayed only once.