# A Program to select iterator values using compress()

from itertools import compress

values = ["Python", "Java", "C++", "Rust", "Go"]

selectors = [1, 0, 1, 0, 1]

selected_values = compress(values, selectors)

for value in selected_values:
    print(value)


# Explanation:
# compress() selects values from one iterable based on corresponding selector values.
# The values iterable contains programming language names.
# The selectors iterable contains truthy and falsy values.
# When a selector is truthy, the corresponding value is included.
# When a selector is falsy, the corresponding value is skipped.
# compress() returns an iterator, so the selected values are produced lazily.

# Real-Life Use:
# compress() is useful when a separate sequence of flags, conditions, or permissions determines which records should be processed.