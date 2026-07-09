# A Program to reverse the order of elements in a list using the reverse() method.

numbers = [10, 20, 30, 40, 50]

print("\nBefore Reverse List is:", numbers)
numbers.reverse()

print("After Reverse List is:", numbers)

# Explanation:
# The program reverses the order of elements in the original list using the reverse() method. Unlike slicing ([::-1]), this method modifies the existing list instead of creating a new one.