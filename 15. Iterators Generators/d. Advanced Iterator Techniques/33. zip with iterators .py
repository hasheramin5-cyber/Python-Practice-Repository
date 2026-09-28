# A Program to combine iterators using zip()

def names():
    yield "Hasher"
    yield "Aadil"
    yield "Hammad"


def scores():
    yield 85
    yield 92
    yield 78


name_iterator = names()
score_iterator = scores()

for name, score in zip(name_iterator, score_iterator):
    print(name, score)


# Explanation:
# zip() combines values from multiple iterables based on their positions.
# The names() generator produces student names.
# The scores() generator produces corresponding scores.
# zip() requests one value from each iterator and combines them into a tuple.
# The process continues until one of the iterators is exhausted.
# The values are processed lazily instead of creating a complete combined collection in memory.

# Real-Life Use:
# zip() with iterators is useful when related data comes from separate streams, files, APIs, or processing stages.