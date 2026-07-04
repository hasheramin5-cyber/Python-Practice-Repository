# Converting between different data types in Python is known as type casting. Here are some examples of type casting in Python:

# String to Integer
string_number = "100"
print(int(string_number), type(int(string_number)))

# Integer to Float
integer_number = 100
print(float(integer_number), type(float(integer_number)))

# Float to Integer
float_number = 99.99
print(int(float_number), type(int(float_number)))

# List to Tuple
my_list = [1, 2, 3]
print(tuple(my_list), type(tuple(my_list)))

# Tuple to List
my_tuple = (4, 5, 6)
print(list(my_tuple), type(list(my_tuple)))

# String to List
text = "Python"
print(list(text), type(list(text)))

# List to Set
duplicate_list = [1, 2, 2, 3, 3, 4]
print(set(duplicate_list), type(set(duplicate_list)))

# Set to List
my_set = {7, 8, 9}
print(list(my_set), type(list(my_set)))

# Integer to String
number = 500
print(str(number), type(str(number)))

# Explaination:
# In this code snippet, we demonstrate various type casting operations in Python. We convert between strings, integers, floats, lists, tuples, and sets using the appropriate type casting functions. Each conversion is followed by printing the converted value and its type to confirm that the conversion was successful.