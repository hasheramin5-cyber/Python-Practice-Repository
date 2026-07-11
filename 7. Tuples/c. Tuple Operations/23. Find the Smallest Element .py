# A Program to find the Smallest Element in a Tuple without using the min() function.

numbers = (45, 12, 89, 23, 67)

print(f"\nTuple: {numbers}")
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest Element:", smallest)

# Explanation:
# The program begins by assuming the first element is the smallest. It then compares every remaining element with the current smallest value. Whenever a smaller element is found, the variable is updated. This exercise demonstrates how searching algorithms work internally and builds a stronger understanding of iteration and comparison.