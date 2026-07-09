# A Program to repeat a list multiple times.

names = ["Hasher", "Amin"]

print(f"Original List: {names}")

repeat = int(input("Enter the number of times to repeat the list: "))
repeated_list = names * repeat

print("Repeated List:", repeated_list)

# Explanation:
# The program demonstrates how the multiplication (*) operator can be used with lists. It first displays the original list and then asks the user how many times the list should be repeated. Python creates a new list by repeating the original list the specified number of times while leaving the original list unchanged. This technique is useful when generating repeated patterns, initializing data, or creating test datasets. It also helps reinforce that the * operator behaves differently for lists than it does for numbers, making it an important concept to understand when working with Python collections.