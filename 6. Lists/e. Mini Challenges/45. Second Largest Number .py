# A Program to find the second largest number in a list.

numbers = [45, 78, 12, 99, 34, 67]

print(f"\nList: {numbers}")
numbers.sort()

print("Second Largest Number:", numbers[-2])

# Explanation:
# The program first sorts the list in ascending order and then accesses the second last element using negative indexing. Since the largest element becomes the last element after sorting, the second last element represents the second largest value. This challenge also reinforces your understanding of sorting and negative indexing in Python.