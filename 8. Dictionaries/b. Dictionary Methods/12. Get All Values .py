# A Program to get all values from a Dictionary.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

values = student.values()

print("Dictionary Values:")
print(values)

# Explanation:
# The program first creates a dictionary containing student information. The values() method retrieves all the values stored in the dictionary without returning their keys. These values are stored in the variable 'values' and then printed. This allows you to work only with the stored data while ignoring the key names.

# Real-Life Use:
# The values() method is useful when calculating totals, averages, statistics, or displaying only the stored information.