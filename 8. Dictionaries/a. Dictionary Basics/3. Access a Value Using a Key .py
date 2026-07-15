# A Program to access a value from a Dictionary using its key.

student = {
    "name": "Hasher",
    "father name": "Amin",
    "age": 20,
    "course": "Python"
}

print("\nStudent Name:", student["name"])

# Explanation:
# The program creates a dictionary named 'student'. After the dictionary is created, Python looks for the key "name" inside it. Since the key exists, Python retrieves its associated value, which is "Hasher", and prints it. Unlike lists, dictionaries do not use numeric indexes. Instead, values are accessed directly through their keys, making the code easier to read.

# Real-Life Use:
# This approach is used in login systems, APIs, and databases where information is retrieved using meaningful names instead of positions.