# A Program to count the number of sentences in a paragraph.

paragraph = input("\nEnter a paragraph: ")

sentences = paragraph.split(".")

count = len(sentences) - 1

print("Number of Sentences =", count)

# Explanation:
# The program counts the number of sentences by splitting the paragraph wherever a period (.) appears. Since split() creates an extra empty element after the last period, one is subtracted from the total count.