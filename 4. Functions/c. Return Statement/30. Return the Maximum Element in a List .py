# A Program to return the maximum element in a list without using max().

def maximum(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

values = [25, 68, 14, 91, 37]

print(f"\nList: {values}")

result = maximum(values)
print("Maximum Element in List =", result)

# Explanation:
# The program defines a function that finds the largest value in a list without using Python's built-in max() function. It assumes the first element is the largest and compares it with every remaining element. Whenever a larger value is found, it becomes the new largest value. After checking all elements, the function returns the maximum element.