# A Program to divide numbers into batches using a generator

def batches(numbers, batch_size):
    for start in range(0, len(numbers), batch_size):
        yield numbers[start:start + batch_size]


numbers = list(range(1, 16))

for batch in batches(numbers, 4):
    print(batch)


# Explanation:
# The batches() generator divides a collection into smaller groups of a specified size.
# The range() function creates starting positions for each batch.
# Slicing is then used to select the values belonging to the current batch.
# Each batch is returned using yield.
# The generator therefore allows the caller to process one batch before requesting the next one.

# Real-Life Use:
# Batching is useful when data must be processed in smaller groups, such as database records, API requests, or machine learning data.