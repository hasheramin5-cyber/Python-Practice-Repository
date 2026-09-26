# A Program to iterate through a tuple using an iterator

languages = ("Python", "C++", "Java", "Go")

language_iterator = iter(languages)

for language in language_iterator:
    print(language)


# Explanation:
# A tuple is also an iterable object.
# iter() creates an iterator from the tuple.
# The for loop then retrieves each tuple element one at a time.
# Because tuples preserve their order, the values are processed in the same order in which they were stored.
# The tuple itself remains unchanged during iteration.

# Real-Life Use:
# Tuple iteration is useful when processing fixed collections of related values.