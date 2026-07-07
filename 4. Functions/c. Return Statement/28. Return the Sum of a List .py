# A Program to return the sum of all elements in a list.

def list_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

values = [10, 20, 30, 40, 50]

print(f"\nList: {values}")

result = list_sum(values)
print("Sum of List =", result)

# Explanation:
# The program defines a function that calculates the sum of all numbers in a list. It uses a loop to add each element to the variable 'total' and then returns the final sum. The returned value can be reused anywhere in the program.