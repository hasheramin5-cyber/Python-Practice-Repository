# A Program to convert a List into a Tuple.

numbers = [10, 20, 30, 40, 50]

numbers_tuple = tuple(numbers)

print("\nOriginal List:", numbers)
print("Converted Tuple:", numbers_tuple)

# Explanation:
# The program converts a list into a tuple using the tuple() function. This is useful when you want to prevent accidental modifications to the data. Once the tuple is created, its elements cannot be changed, making it suitable for storing fixed information.