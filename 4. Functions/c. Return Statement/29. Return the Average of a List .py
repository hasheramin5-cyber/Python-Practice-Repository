# A Program to return the average of all elements in a list.

def average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)

values = [12, 15, 18, 21, 24]

print(f"\nList: {values}")

result = average(values)
print("Average of List =", result)

# Explanation:
# The program defines a function that calculates the average of the numbers in a list. It first finds the total of all elements using a loop and then divides the total by the number of elements in the list. The calculated average is returned and displayed.