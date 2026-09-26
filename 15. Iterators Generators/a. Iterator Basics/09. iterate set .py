# A Program to iterate through a set using an iterator

skills = {"Python", "Git", "PyTorch", "OpenCV", "GitHub"}

skills_iterator = iter(skills)

for skill in skills_iterator:
    print(skill)


# Explanation:
# A set is iterable, so iter() can create an iterator over its elements.
# The for loop retrieves each element one at a time.
# Unlike lists and tuples, sets are unordered collections.
# Therefore, we should not depend on the order in which the values are printed.
# The main purpose here is to understand that different Python collection types can provide iterators.

# Real-Life Use:
# Set iteration is useful when processing unique values without requiring a specific order.