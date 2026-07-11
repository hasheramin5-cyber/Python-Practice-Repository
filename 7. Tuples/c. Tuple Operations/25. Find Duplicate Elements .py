# A Program to find Duplicate Elements in a Tuple.

numbers = (10, 20, 30, 20, 40, 10, 50, 30)

print(f"\nTuple: {numbers}")
duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Duplicate Elements:", duplicates)

# Explanation:
# The program checks every element in the tuple to determine whether it appears more than once. If an element occurs multiple times and has not already been added to the duplicates list, it is stored. Identifying duplicate values is useful in data cleaning, database management, and quality assurance tasks.