# A Program to Swap Two Variables using Tuple unpacking.

a = 10
b = 20

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter Swapping:")
print("a =", a)
print("b =", b)

# Explanation:
# The program swaps the values of two variables without using a third variable. Python first creates a temporary tuple containing the values (b, a). It then unpacks those values back into the variables 'a' and 'b'. As a result, the values are exchanged in a single statement. This is one of Python's most popular and elegant features.