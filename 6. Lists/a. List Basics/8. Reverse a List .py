# A Program to reverse a list.

numbers = [10, 20, 30, 40, 50]

reversed_list = numbers[::-1]

print("\nOriginal List is:", numbers)
print("Reversed List is:", reversed_list)

# Explanation:
# The program reverses the order of the list using slicing. The slice [::-1] starts from the last element and moves backward one element at a time, producing a reversed copy of the original list without changing it.