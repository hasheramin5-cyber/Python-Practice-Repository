# A Program to analyze quiz scores.

scores = (78, 85, 92, 88, 95)

print(f"\nScores: {scores}")

print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))
print("Average Score:", sum(scores) / len(scores))

# Explanation:
# The program stores quiz scores inside a tuple. It uses Python's built-in functions to calculate the highest score, lowest score, and average score. Since quiz results usually remain unchanged after evaluation, storing them inside a tuple makes the data safe from accidental modification.