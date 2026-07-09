# A Program to find the smallest element in a list without using the min() function.

numbers = [45, 12, 89, 23, 67]

print(f"\nList: {numbers}")
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest Element is:", smallest)

# Explanation:
# The program assumes the first element is the smallest. It then compares every remaining element with the current smallest value. Whenever a smaller element is found, it becomes the new smallest element.