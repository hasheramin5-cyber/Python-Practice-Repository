# A Program to find the largest number in a list without using max().

numbers = [12, 45, 8, 91, 27, 64]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest Number =", largest)

# Explanation:
# The program finds the largest number in a list without using Python's built-in max() function. It assumes the first element is the largest and compares it with every remaining element. Whenever a larger number is found, it becomes the new largest value. After checking all elements, the largest number is displayed.