# A Program to check whether an Element exists in a Tuple or not.

languages = ("Python", "Java", "C++", "JavaScript")

print(f"\nTuple: {languages}")

language = input("\nEnter a programming language: ").title()

if language in languages:
    print(language, "exists in the tuple.")
else:
    print(language, "does not exist in the tuple.")

# Explanation:
# The program uses the 'in' operator to check whether a given element exists in the tuple. Membership testing is a fast and readable way to verify the presence of data. This concept is widely used when validating user input, searching collections, and implementing access-control or lookup systems.