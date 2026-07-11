# A Program to find the Largest Element in a Tuple without using the max() function.

numbers = (45, 12, 89, 23, 67)

print(f"\nTuple: {numbers}")
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest Element:", largest)

# Explanation:
# The program assumes the first element is the largest and then compares every remaining element with it. Whenever a larger value is found, the variable is updated. This manual approach helps you understand the logic behind searching algorithms instead of depending on Python's built-in max() function. Learning this technique strengthens your problem-solving skills and prepares you for technical interviews.