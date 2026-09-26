# A Program to iterate through a string using an iterator

text = "Python"

text_iterator = iter(text)

for character in text_iterator:
    print(character)


# Explanation:
# Strings are iterable objects in Python.
# Calling iter() on the string creates an iterator that produces one character at a time.

# The for loop retrieves each character sequentially:
# P --> y --> t --> h --> o --> n
# The original string is not changed during iteration.

# Real-Life Use:
# Character-by-character iteration is useful for text processing, validation, searching, and parsing.