# A Program to find the largest element in a list without using the max() function.

numbers = [45, 12, 89, 23, 67]

print(f"\nList: {numbers}")
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest Element is:", largest)

# Explanation:
# The program assumes the first element is the largest. It then compares every remaining element with the current largest value. Whenever a larger element is found, it becomes the new largest element.