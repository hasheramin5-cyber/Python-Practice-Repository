# A Program to get all key-value pairs using the items() method.

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Python"
}

items = student.items()

print("\nDictionary Items:")
print(items)

# Explanation:
# The program creates a dictionary and calls the items() method. This method returns every key together with its corresponding value as tuple pairs. The result is stored in the variable 'items' and then displayed. The items() method is especially useful when both keys and values need to be processed together inside loops.

# Real-Life Use:
# The items() method is frequently used while generating reports, displaying user profiles, and processing JSON or API data.